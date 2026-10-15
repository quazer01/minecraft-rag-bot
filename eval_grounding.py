"""Grounding eval: are CraftGuide's answers correct and taken from the library?

    python eval_grounding.py                       # qwen2.5:3b, 3 trials per case
    python eval_grounding.py --model llama3.2 --trials 1 --out runs/llama.jsonl

Each Minecraft answer is scored correct (every required fact, no fabrication), "couldn't find", or wrong.
Points: correct 2, couldn't find 1, wrong 0, so a wrong answer costs more than admitting the gap.
Chat cases (small talk, memory, off-topic) are a pass/fail gate scored separately.
"""

import argparse
import json
import re
import statistics
import sys
import time
from dataclasses import dataclass, field

from rag import OLLAMA_MODEL, ChatSession, open_session

COULDNT_FIND = re.compile(r"couldn'?t find|could not find|can'?t find|not (?:in|covered by) my (?:minecraft )?"
                          r"(?:knowledge|library)|don'?t have (?:that|any|information)", re.I)


@dataclass(frozen=True)
class Fact:
    """A Minecraft answer: every group in `required` must match, nothing in `forbidden` may."""
    required: tuple[str, ...]
    forbidden: tuple[str, ...] = ()


@dataclass(frozen=True)
class Chat:
    """A non-Minecraft answer: no retrieval, must match `contains`, must not match `forbidden`."""
    contains: str = ""
    forbidden: tuple[str, ...] = ()


@dataclass(frozen=True)
class Turn:
    message: str
    expect: Fact | Chat | None = None  # None: a setup turn, not scored


@dataclass(frozen=True)
class Case:
    name: str
    turns: tuple[Turn, ...]
    history: tuple[tuple[str, str], ...] = field(default=())  # seeded (user, assistant) exchanges

    def __post_init__(self) -> None:
        if not (isinstance(self.turns, tuple) and all(isinstance(t, Turn) for t in self.turns)):
            raise TypeError(f"case {self.name!r}: turns must be a tuple of Turn, got {self.turns!r:.80}")


WRONG_GOLEM = ("To build an Iron Golem you need 4 iron ingots and 10 iron blocks. Place them in a T-shape with the "
               "iron ingots at the center. [Source: Mobs (Creatures) > Neutral mobs]")
GOLEM = Fact((r"iron blocks?", r"pumpkin"), (r"iron ingots? (?:at|in) the cent", r"\b10 iron", r"\b4 iron ingots"))
WITHER_JAVA = Fact((r"\b300\b",), (r"\b600\b(?!.*bedrock)",))
WITHER_BEDROCK = Fact((r"\b600\b",))

CASES: tuple[Case, ...] = (
    Case("iron golem", (Turn("how can I made iron golem", GOLEM),)),
    Case("snow golem", (Turn("how do I build a snow golem?",
                             Fact((r"(?:2|two) snow blocks?", r"pumpkin"), (r"\b[3-9] snow blocks?", r"iron"))),)),
    Case("bed", (Turn("how do I craft a bed?", Fact((r"\b(?:3|three) (?:pieces of )?wool", r"planks?"),
                                                     (r"\b[4-9] wool", r"\bstring"))),)),
    Case("enchanting table", (Turn("How do I craft an enchanting table?",
                                   Fact((r"\bbook", r"diamonds?", r"obsidian"),
                                        (r"\b(?:3|5|6|8) obsidian", r"\b[3-9] diamonds"))),)),
    Case("creeper HP", (Turn("how much health does a creeper have?", Fact((r"\b20\b",), (r"\b40\b",))),)),
    Case("enderman", (Turn("How much health does an Enderman have and what does it drop?",
                           Fact((r"\b40\b", r"ender ?pearls?"), (r"\b(?:20|60|80) (?:hp|health)",))),)),
    Case("iron golem HP", (Turn("how much health does an iron golem have?", Fact((r"\b100\b",))),)),
    Case("blaze drop", (Turn("what does a blaze drop?", Fact((r"blaze rods?",))),)),
    Case("trident mob", (Turn("which mob can drop a trident?", Fact((r"drowned",))),)),
    Case("/tp", (Turn("How do I teleport to another player with a command?",
                      Fact((r"/tp\b|/teleport\b",), (r"/warp\b", r"/goto\b"))),)),
    Case("diamond Y", (Turn("what is the best Y level for diamonds?",
                            Fact((r"[-−–]\s?59\b",), (r"\by\s*=?\s*1[12]\b", r"level 1[12]\b"))),)),
    Case("ancient debris Y", (Turn("what Y level is best for ancient debris?", Fact((r"\b15\b",))),)),
    Case("netherite upgrade", (Turn("how do I upgrade diamond armor to netherite?",
                                    Fact((r"smithing table", r"template", r"netherite ingot"), (r"\banvil",))),)),
    Case("netherite durability", (Turn("what is the durability of netherite tools?", Fact((r"2,?031",))),)),
    Case("piston push", (Turn("how many blocks can a piston push?", Fact((r"\b12\b",))),)),
    Case("wither summon", (Turn("how do I summon the wither?",
                                Fact((r"soul (?:sand|soil)", r"wither skeleton skulls?"),
                                     (r"\b[1245] wither skeleton skulls?",))),)),
    Case("redstone Java vs Bedrock", (Turn("What are the differences between Java and Bedrock redstone?",
                                           Fact((r"quasi[- ]?connectivity",))),)),
    Case("Bedrock server port", (Turn("what port does a Bedrock server use?", Fact((r"19132",))),)),
    Case("wither Bedrock HP", (Turn("how much health does the wither have in Bedrock?", Fact((r"\b600\b",))),)),
    Case("follow-up: what about in Bedrock?", (Turn("How much health does the Wither have?", WITHER_JAVA),
                                               Turn("what about in Bedrock?", WITHER_BEDROCK))),
    Case("follow-up: dispute after own answer", (Turn("how can I made iron golem", GOLEM),
                                                 Turn("no u are wrong", GOLEM))),
    Case("follow-up: dispute after a wrong answer", (Turn("no u are wrong", GOLEM),),
         history=(("how can I made iron golem", WRONG_GOLEM),)),
    Case("follow-up: that's not right", (Turn("that's not right", Fact((r"\b20\b",), (r"\b40\b",))),),
         history=(("how much health does a creeper have?",
                   "A creeper has 40 health points. [Source: Mobs (Creatures) > Hostile mobs]"),)),
    Case("small talk", (Turn("hi, how are you?", Chat(forbidden=(r"\[source",))),)),
    Case("thanks", (Turn("thanks!", Chat(forbidden=(r"\[source",))),)),
    Case("memory", (Turn("my name is Jean"), Turn("what's my name?", Chat(contains=r"\bJean\b")))),
    Case("off-topic: capital", (Turn("What is the capital of France?",
                                     Chat(contains=r"minecraft", forbidden=(r"paris",))),)),
    Case("off-topic: homework", (Turn("solve x^2 = 9", Chat(contains=r"minecraft",
                                                            forbidden=(r"x\s*=\s*[-±]?\s*3\b", r"±\s*3"))),)),
)


def score_fact(expect: Fact, answer: str) -> str:
    if any(re.search(p, answer, re.I | re.S) for p in expect.forbidden):
        return "wrong"
    if all(re.search(p, answer, re.I) for p in expect.required):
        return "correct"
    return "couldn't find" if COULDNT_FIND.search(answer) else "wrong"


def score_chat(expect: Chat, answer: str, retrieved: bool) -> str:
    ok = (not retrieved and (not expect.contains or re.search(expect.contains, answer, re.I))
          and not any(re.search(p, answer, re.I) for p in expect.forbidden))
    return "pass" if ok else "fail"


def where_facts_sit(expect: Fact, chunks) -> list[dict]:
    """For each required fact: the first retrieved chunk and line that contains it, or None."""
    found = []
    for pattern in expect.required:
        spot = None
        for rank, chunk in enumerate(chunks):
            for line_no, line in enumerate(chunk.text.splitlines()):
                if re.search(pattern, line, re.I):
                    spot = {"chunk": rank, "title": chunk.source_title, "line": line_no,
                            "lines_in_chunk": len(chunk.text.splitlines())}
                    break
            if spot:
                break
        found.append({"fact": pattern, "at": spot})
    return found


def run_case(base: ChatSession, case: Case, errors: list) -> list[dict]:
    session = ChatSession(base.backend, base.ollama,
                          history=[{"role": r, "content": c} for u, a in case.history
                                   for r, c in (("user", u), ("assistant", a))])
    rows = []
    for turn in case.turns:
        failed_before = len(errors)
        start = time.perf_counter()
        result = session.ask(turn.message)
        seconds = time.perf_counter() - start
        if turn.expect is None:
            continue
        row = {"case": case.name, "message": turn.message, "route": result.route.kind,
               "search_query": result.route.search_query, "retrieved": [c.source_title for c in result.chunks],
               "answer": result.answer, "seconds": round(seconds, 2), "ollama_failed": len(errors) > failed_before}
        if isinstance(turn.expect, Fact):
            row |= {"kind": "fact", "verdict": score_fact(turn.expect, result.answer),
                    "facts_in_context": where_facts_sit(turn.expect, result.chunks)}
        else:
            row |= {"kind": "chat", "verdict": score_chat(turn.expect, result.answer, bool(result.chunks))}
        rows.append(row)
    return rows


POINTS = {"correct": 2, "couldn't find": 1, "wrong": 0}


def recording_errors(transport, errors: list):
    def send(path, payload, timeout):
        try:
            return transport(path, payload, timeout)
        except Exception as e:
            errors.append(e)
            raise
    return send


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--model", default=OLLAMA_MODEL)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--only", help="run only cases whose name contains this text")
    parser.add_argument("--out", help="write every scored turn as JSON lines to this file")
    args = parser.parse_args()

    base, status = open_session("ollama", args.model)
    print(status)
    if base.backend != "ollama":
        return 2
    errors: list[Exception] = []
    base.ollama.transport = recording_errors(base.ollama.transport, errors)
    cases = [c for c in CASES if not args.only or args.only in c.name]

    rows = []
    for trial in range(args.trials):
        for case in cases:
            for row in run_case(base, case, errors):
                rows.append(row | {"trial": trial})
                print(f"[{trial}] {row['verdict']:>13}  {case.name}: {row['message']!r} ({row['seconds']}s)")
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)

    facts = [r for r in rows if r["kind"] == "fact"]
    chats = [r for r in rows if r["kind"] == "chat"]
    counts = {v: sum(r["verdict"] == v for r in facts) for v in POINTS}
    score = sum(POINTS[r["verdict"]] for r in facts) / (2 * len(facts))
    passes = sum(r["verdict"] == "pass" for r in chats)
    print(f"\nmodel {args.model}, {args.trials} trials, {len(rows)} scored answers, {len(errors)} Ollama errors")
    print("per case (correct/couldn't find/wrong or pass/fail across trials):")
    for case in cases:
        for message in dict.fromkeys(r["message"] for r in rows if r["case"] == case.name):
            verdicts = [r["verdict"] for r in rows if r["case"] == case.name and r["message"] == message]
            print(f"  {case.name} / {message!r}: {', '.join(verdicts)}")
    correct, unknown, wrong = counts.values()
    print(f"grounding score {score:.1%}  (correct {correct}, couldn't find {unknown}, wrong {wrong} of {len(facts)})")
    print(f"chat gate {passes}/{len(chats)} pass")
    print(f"median seconds per answer {statistics.median(r['seconds'] for r in rows):.1f}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
