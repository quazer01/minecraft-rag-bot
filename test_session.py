"""Offline checks of ChatSession wiring with a fake Claude client. No API key needed.

    python test_session.py
"""

import builtins
import io
import json
import sys
from contextlib import redirect_stdout
from types import SimpleNamespace

import chat
import rag
from rag import HISTORY_LIMIT, NO_DOCUMENTS, SYSTEM_TEMPLATE, ChatSession, RetrievedChunk

BED = RetrievedChunk("Crafting > Useful recipes (written)", "both", "26.3", "| Bed | 3 wool + 3 planks |", 0.4)


class FakeClaude:
    """Routes messages that mention 'craft' to minecraft and everything else to chitchat."""

    def __init__(self) -> None:
        self.answer_requests: list[dict] = []
        self.messages = self

    def create(self, **request):
        if "output_config" in request:
            latest = request["messages"][0]["content"].rsplit("Latest message: ", 1)[1]
            route = ({"kind": "minecraft", "search_query": f"{latest} recipe"} if "craft" in latest
                     else {"kind": "chitchat", "search_query": ""})
            text = json.dumps(route)
        else:
            self.answer_requests.append(request)
            text = f"answer {len(self.answer_requests)}"
        return SimpleNamespace(content=[SimpleNamespace(type="text", text=text)])


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
    fake = FakeClaude()
    session = ChatSession("claude", client=fake)

    turn = session.ask("hi, how are you?")
    system = fake.answer_requests[-1]["system"]
    check(turn.route.kind == "chitchat" and not turn.chunks and not queries, "chitchat skips retrieval")
    check(f"<context>\n{NO_DOCUMENTS}\n</context>" in system, "chitchat fills the placeholder documents")

    turn = session.ask("how do I craft a bed?")
    request = fake.answer_requests[-1]
    check(queries == ["how do I craft a bed? recipe"], "minecraft retrieves with the router's search query")
    check("Source title: Crafting > Useful recipes (written)" in request["system"], "retrieved chunks carry their source title")
    head, tail = SYSTEM_TEMPLATE.split("{retrieved_documents}")
    check(request["system"].startswith(head) and request["system"].endswith(
        tail.replace("{user_question}", "how do I craft a bed?")), "system prompt is the template with both slots filled")
    check([m["content"] for m in request["messages"]] == ["hi, how are you?", "answer 1", "how do I craft a bed?"],
          "earlier turns are sent as history before the new message")

    for i in range(15):
        session.ask(f"message {i}")
    sent = fake.answer_requests[-1]["messages"]
    check(len(session.history) == HISTORY_LIMIT, f"history is capped at {HISTORY_LIMIT} messages")
    check(len(sent) == HISTORY_LIMIT + 1 and sent[0] == {"role": "user", "content": "message 4"},
          "the oldest messages drop off and the window still starts with a user message")

    chat_fake = FakeClaude()
    chat.ChatSession = lambda backend: ChatSession("claude", client=chat_fake)
    lines = iter(["my name is Jean", "/reset", "hello again", "/quit"])
    with redirect_stdout(io.TextIOWrapper(io.BytesIO(), encoding="utf-8")):
        builtins_input, builtins.input = builtins.input, lambda prompt="": next(lines)
        try:
            chat.main()
        finally:
            builtins.input = builtins_input
    check(chat_fake.answer_requests[-1]["messages"] == [{"role": "user", "content": "hello again"}],
          "/reset in the chat clears the history")

    check(rag.parse_route("not json", "q") == rag.Route("minecraft", "q"),
          "a malformed router reply falls back to retrieving the raw question")

    print(f"\n{check.failures} failed" if check.failures else "\nall checks passed")
    return 1 if check.failures else 0


if __name__ == "__main__":
    sys.exit(main())
