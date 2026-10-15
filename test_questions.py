"""End-to-end checks: ask CraftGuide real questions and conversations, then check the answers.

    python test_questions.py                  # every check; needs Ollama with the model pulled
    python test_questions.py --model llama3.2 # the same checks with another Ollama model
    python test_questions.py --retrieval-only # retrieval checks only, no Ollama needed
"""

import argparse
import sys
from dataclasses import dataclass

from rag import OLLAMA_MODEL, ChatSession, Turn, open_session, retrieve


@dataclass(frozen=True)
class Step:
    message: str
    retrieves: bool | None = None
    retrieval_must_contain: str | None = None
    cites: bool | None = None
    answer_contains_any: tuple[str, ...] = ()
    answer_excludes: tuple[str, ...] = ()


CONVERSATIONS: dict[str, list[Step]] = {
    "crafting recipe": [Step("How do I craft an enchanting table?", retrieves=True,
                             retrieval_must_contain="Enchanting table", cites=True,
                             answer_contains_any=("obsidian",))],
    "mob": [Step("How much health does an Enderman have and what does it drop?", retrieves=True,
                 retrieval_must_contain="Enderman", cites=True, answer_contains_any=("40", "ender pearl"))],
    "command": [Step("How do I teleport to another player with a command?", retrieves=True,
                     retrieval_must_contain="/tp", cites=True, answer_contains_any=("/tp",))],
    "Java vs Bedrock": [Step("What are the differences between Java and Bedrock redstone?", retrieves=True,
                             retrieval_must_contain="Java vs Bedrock redstone differences", cites=True,
                             answer_contains_any=("Bedrock",))],
    "non-Minecraft fact": [Step("What is the capital of France?",
                                answer_contains_any=("Minecraft",), answer_excludes=("Paris",))],
    "greeting": [Step("hi, how are you?", retrieves=False, cites=False)],
    "memory": [Step("my name is Jean", retrieves=False),
               Step("what's my name?", retrieves=False, answer_contains_any=("Jean",))],
    "bed recipe": [Step("how do I craft a bed?", retrieves=True, retrieval_must_contain="3 wool (top row)",
                        cites=True, answer_contains_any=("wool",))],
    "homework": [Step("solve x^2 = 9", answer_contains_any=("Minecraft",),
                      answer_excludes=("±3", "x = 3", "x=3", "x = -3", "x=-3"))],
}


def contains(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def retrieval_check(step: Step, chunks) -> bool:
    return any(contains(f"{c.source_title}\n{c.text}", step.retrieval_must_contain) for c in chunks)


def answer_checks(step: Step, turn: Turn) -> dict[str, bool]:
    checks = {}
    if step.retrieves is not None:
        checks["retrieves" if step.retrieves else "skips retrieval"] = bool(turn.chunks) == step.retrieves
    if step.retrieval_must_contain:
        checks[f"retrieved {step.retrieval_must_contain!r}"] = retrieval_check(step, turn.chunks)
    if step.cites is not None:
        checks["cites a source" if step.cites else "no citations"] = contains(turn.answer, "[Source:") == step.cites
    if step.answer_contains_any:
        checks[f"mentions one of {step.answer_contains_any}"] = any(
            contains(turn.answer, n) for n in step.answer_contains_any)
    for needle in step.answer_excludes:
        checks[f"does not say {needle!r}"] = not contains(turn.answer, needle)
    return checks


def run_conversation(base: ChatSession, steps: list[Step]) -> dict[str, bool]:
    session, results = ChatSession(base.backend, base.ollama), {}
    for step in steps:
        turn = session.ask(step.message)
        print(f"  You: {step.message}\n  [{turn.route.kind}] "
              f"retrieved: {[c.source_title for c in turn.chunks]}\n"
              "  CraftGuide: " + turn.answer.replace("\n", "\n    "))
        results |= {f"{step.message!r}: {name}": ok for name, ok in answer_checks(step, turn).items()}
    return results


def recording_errors(transport, errors: list[Exception]):
    def send(path, payload, timeout):
        try:
            return transport(path, payload, timeout)
        except Exception as e:
            errors.append(e)
            raise
    return send


def run_retrieval_only(steps: list[Step]) -> dict[str, bool]:
    results = {}
    for step in steps:
        if step.retrieval_must_contain:
            chunks = retrieve(step.message)
            print(f"  retrieved: {[c.source_title for c in chunks]}")
            results[f"{step.message!r}: retrieved {step.retrieval_must_contain!r}"] = retrieval_check(step, chunks)
    return results


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--retrieval-only", action="store_true")
    parser.add_argument("--model", default=OLLAMA_MODEL, help="the Ollama model (default: %(default)s)")
    args = parser.parse_args()

    ollama_errors: list[Exception] = []
    if args.retrieval_only:
        print("Retrieval checks only (no language model).")
    else:
        base, status = open_session("ollama", args.model)
        print(status)
        if base.backend != "ollama":
            print("These checks need the ollama backend; fix the above, or run with --retrieval-only.")
            return 2
        base.ollama.transport = recording_errors(base.ollama.transport, ollama_errors)

    results: dict[str, bool] = {}
    for name, steps in CONVERSATIONS.items():
        print(f"\n[{name}]")
        outcome = run_retrieval_only(steps) if args.retrieval_only else run_conversation(base, steps)
        for check, ok in outcome.items():
            print(f"  {'PASS' if ok else 'FAIL'}  {check}")
        results |= {f"{name} / {check}": ok for check, ok in outcome.items()}

    if ollama_errors:
        print(f"\n{len(ollama_errors)} Ollama calls failed, so those turns were answered offline and the "
              f"results don't measure {args.model}. First error: {ollama_errors[0]!r}")
        return 2
    failures = [check for check, ok in results.items() if not ok]
    print(f"\n{len(results) - len(failures)} checks passed, {len(failures)} failed")
    for check in failures:
        print(f"  FAIL  {check}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
