"""Checks of ChatSession wiring with a fake Ollama transport. No network and no Ollama needed.

    python test_session.py
"""

import builtins
import io
import json
import sys
from contextlib import redirect_stdout
from urllib.error import URLError

import chat
import offline
import rag
from rag import HISTORY_LIMIT, NO_DOCUMENTS, ROUTE_SCHEMA, SYSTEM_TEMPLATE, ChatSession, Ollama, resolve_backend

BED = rag.RetrievedChunk("Crafting > Useful recipes (written)", "both", "26.3",
                         "| Item | Ingredients |\n|---|---|\n| Bed | 3 wool + 3 planks |", 0.4)


class FakeOllama:
    """An Ollama transport. The router sends messages that mention 'craft' to minecraft, everything else to chitchat."""

    def __init__(self, models=("qwen2.5:3b",)) -> None:
        self.models = models
        self.route_requests: list[dict] = []
        self.answer_requests: list[dict] = []
        self.down = False

    def __call__(self, path: str, payload: dict | None) -> dict:
        if self.down:
            raise URLError("connection refused")
        if path == "/api/tags":
            return {"models": [{"name": name, "model": name} for name in self.models]}
        if "format" in payload:
            self.route_requests.append(payload)
            latest = payload["messages"][-1]["content"].rsplit("Latest message: ", 1)[1]
            route = ({"kind": "minecraft", "search_query": f"{latest} recipe"} if "craft" in latest
                     else {"kind": "chitchat", "search_query": ""})
            content = json.dumps(route)
        else:
            self.answer_requests.append(payload)
            content = f"answer {len(self.answer_requests)}"
        return {"model": payload["model"], "message": {"role": "assistant", "content": content}, "done": True}


def dead(path: str, payload: dict | None) -> dict:
    raise URLError("connection refused")


def check(ok: bool, message: str) -> None:
    print(f"{'PASS' if ok else 'FAIL'}  {message}")
    if not ok:
        check.failures += 1


check.failures = 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.argv = sys.argv[:1]
    queries: list[str] = []
    rag.retrieve = lambda query: queries.append(query) or [BED]

    fake = FakeOllama()
    session = ChatSession("ollama", Ollama("qwen2.5:3b", transport=fake))
    turn = session.ask("hi, how are you?")
    system = fake.answer_requests[-1]["messages"][0]
    check(turn.route.kind == "chitchat" and not turn.chunks and not queries, "chitchat skips retrieval")
    check(system["role"] == "system" and f"<context>\n{NO_DOCUMENTS}\n</context>" in system["content"],
          "chitchat fills the placeholder documents")

    turn = session.ask("how do I craft a bed?")
    request = fake.answer_requests[-1]
    system = request["messages"][0]["content"]
    check(queries == ["how do I craft a bed? recipe"], "minecraft retrieves with the router's search query")
    check("Source title: Crafting > Useful recipes (written)" in system, "retrieved chunks carry their source title")
    head, tail = SYSTEM_TEMPLATE.split("{retrieved_documents}")
    check(system.startswith(head) and system.endswith(tail.replace("{user_question}", "how do I craft a bed?")),
          "system prompt is the template with both slots filled")
    check([m["content"] for m in request["messages"][1:]] == ["hi, how are you?", "answer 1", "how do I craft a bed?"],
          "earlier turns are sent as history before the new message")
    check(request["options"] == {"temperature": 0.3, "num_ctx": 8192} and request["stream"] is False
          and "format" not in request, "the answer request asks for temperature 0.3, an 8192 context, no streaming")
    route_request = fake.route_requests[-1]
    check(route_request["format"] == ROUTE_SCHEMA and route_request["options"]["temperature"] == 0
          and route_request["messages"][0] == {"role": "system", "content": rag.ROUTER_INSTRUCTIONS},
          "the router request carries the route schema as format, at temperature 0")

    for i in range(15):
        session.ask(f"message {i}")
    sent = fake.answer_requests[-1]["messages"][1:]
    check(len(session.history) == HISTORY_LIMIT, f"history is capped at {HISTORY_LIMIT} messages")
    check(len(sent) == HISTORY_LIMIT + 1 and sent[0] == {"role": "user", "content": "message 4"},
          "the oldest messages drop off and the window still starts with a user message")

    chat_fake = FakeOllama()
    chat.open_session = lambda backend, model: (ChatSession("ollama", Ollama(transport=chat_fake)), "")
    lines = iter(["my name is Jean", "/reset", "hello again", "/quit"])
    with redirect_stdout(io.TextIOWrapper(io.BytesIO(), encoding="utf-8")):
        builtins_input, builtins.input = builtins.input, lambda prompt="": next(lines)
        try:
            chat.main()
        finally:
            builtins.input = builtins_input
    check(chat_fake.answer_requests[-1]["messages"][1:] == [{"role": "user", "content": "hello again"}],
          "/reset in the chat clears the history")

    check(rag.parse_route("not json", "q") == rag.Route("minecraft", "q"),
          "a malformed router reply falls back to retrieving the raw question")

    # Choosing the backend at startup.
    backend, status = resolve_backend("auto", Ollama("qwen2.5:3b", transport=dead))
    check(backend == "offline" and "ollama serve" in status and "ollama pull qwen2.5:3b" in status,
          "auto with Ollama down is offline, and the startup line says how to fix it")
    check(resolve_backend("ollama", Ollama("qwen2.5:3b", transport=dead))[0] == "offline",
          "an explicit ollama backend with Ollama down still falls back to offline")
    backend, status = resolve_backend("auto", Ollama("llama3.2", transport=FakeOllama(models=("qwen2.5:3b",))))
    check(backend == "offline" and "ollama pull llama3.2" in status,
          "auto with the model not pulled is offline and names the pull command")
    check(resolve_backend("auto", Ollama("llama3.2", transport=FakeOllama(models=("llama3.2:latest",))))[0] == "ollama",
          "a model pulled as name:latest counts as present")
    check(resolve_backend("auto", Ollama("qwen2.5:3b", transport=FakeOllama())) == ("ollama", "CraftGuide: Ollama · qwen2.5:3b"),
          "auto with Ollama up and the model pulled is ollama")

    # Ollama stops after startup.
    queries.clear()
    dying = FakeOllama()
    session = ChatSession("ollama", Ollama(transport=dying))
    session.ask("hi")
    dying.down = True
    turn = session.ask("how do I craft a bed?")
    check(turn.answer == offline.answer("how do I craft a bed?", [BED]) and "[Source:" in turn.answer
          and queries == ["how do I craft a bed?"], "a question asked after Ollama stops is answered offline")
    check(len(session.history) == 4 and session.history[-1]["content"] == turn.answer,
          "the offline turn joins the history")
    malformed = ChatSession("ollama", Ollama(transport=lambda path, payload: {"message": {"content": None}}))
    check(malformed.ask("thanks!").answer == "You're welcome! Happy crafting.",
          "a malformed Ollama reply is answered offline")

    # Offline mode: scripted small talk, otherwise the library.
    queries.clear()
    calls: list[str] = []
    session = ChatSession("offline", Ollama(transport=lambda path, payload: calls.append(path) or {}))
    say = session.ask
    turn = say("hi, how are you?")
    check(turn.route.kind == "chitchat" and turn.answer and not turn.chunks and not queries,
          "offline small talk answers 'how are you' without retrieval")
    check(say("what's my name?").answer.startswith("I don't know your name"),
          "offline, asking for a name never given says it isn't known yet")
    check("Jean" in say("my name is Jean").answer, "offline, 'my name is Jean' greets Jean")
    check("Jean" in say("what's my name?").answer, "offline, 'what's my name?' answers with the name given")
    say("my name is Marie")
    say("thanks")
    check("Marie" in say("what's my name?").answer, "offline, the newest 'my name is' wins")
    replies = {say(m).answer for m in ("thanks!", "bye", "who are you?", "hello")}
    check(len(replies) == 4 and not queries, "thanks, bye, who are you and hello each get their own reply")
    check("offline" in say("who are you?").answer, "'who are you' says the bot is offline")
    turn = say("how do I craft a bed?")
    check(turn.route == rag.Route("minecraft", "how do I craft a bed?") and queries == ["how do I craft a bed?"]
          and turn.answer == offline.answer("how do I craft a bed?", [BED]),
          "offline, a Minecraft question goes through retrieval and the library answer")
    check(say("hi, how do I craft a bed?").route.kind == "minecraft",
          "offline, a question that opens with a greeting is still searched")
    check(not calls, "the offline backend never calls Ollama")

    # Small talk is a pure function of the message and the history, so the stateless web server gets it too.
    session = ChatSession("offline", Ollama(transport=dead),
                          history=[{"role": "user", "content": "Hi, my name is Jean!"},
                                   {"role": "assistant", "content": "Nice to meet you."}])
    check("Jean" in session.ask("what's my name?").answer, "offline, the name is read back from the history")

    print(f"\n{check.failures} failed" if check.failures else "\nall checks passed")
    return 1 if check.failures else 0


if __name__ == "__main__":
    sys.exit(main())
