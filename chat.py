"""Command-line chat with CraftGuide, the Minecraft RAG bot."""

import argparse
import sys

from rag import BACKEND, BACKEND_CHOICES, OLLAMA_MODEL, open_session


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")  # the data uses symbols like × that cp1252 can't print
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--debug", action="store_true",
                        help="show each message's route, search query and retrieved sources")
    parser.add_argument("--backend", default=BACKEND, choices=BACKEND_CHOICES,
                        help="auto uses Ollama when it is running and has the model, offline otherwise")
    parser.add_argument("--model", default=OLLAMA_MODEL, help="the Ollama model (default: %(default)s)")
    args = parser.parse_args()

    session, status = open_session(args.backend, args.model)
    print(status)
    print("Ask me anything about Minecraft, or just chat. Type /reset to start over, /quit to exit.")
    while True:
        try:
            question = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not question:
            continue
        if question.lower() in {"/quit", "quit", "exit"}:
            break
        if question.lower() == "/reset":
            session.history.clear()
            print("CraftGuide: Conversation cleared.")
            continue

        turn = session.ask(question)
        if args.debug:
            print(f"  [route] {turn.route.kind}" +
                  (f", search query: {turn.route.search_query}" if turn.route.search_query else ""))
            for chunk in turn.chunks:
                print(f"  [retrieved] {chunk.source_title} ({chunk.edition}, {chunk.game_version or 'no version'})")
        print(f"\nCraftGuide: {turn.answer}")


if __name__ == "__main__":
    main()
