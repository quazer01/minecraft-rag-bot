"""A small local web chat for CraftGuide (Python standard library only).

    python server.py                      # then open http://localhost:8000
    python server.py --port 8080 --backend offline
    python server.py --model llama3.2

The server keeps no conversation state: the page sends the history with every message,
so several browser tabs can chat at once.
"""

import argparse
import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from ingest import ROOT, get_collection, ingest
from rag import BACKEND, BACKEND_CHOICES, HISTORY_LIMIT, OLLAMA_MODEL, ChatSession, open_session

PAGE = ROOT / "web" / "index.html"
MAX_MESSAGE_CHARS = 2000
SESSION: ChatSession  # set in main(); its backend and Ollama client are shared by every request


def parse_history(raw) -> list[dict[str, str]]:
    """Keep only well-formed user/assistant pairs from the page, newest last, capped like ChatSession."""
    if not isinstance(raw, list):
        return []
    pairs = []
    for user, bot in zip(raw[::2], raw[1::2]):
        if (isinstance(user, dict) and isinstance(bot, dict) and user.get("role") == "user"
                and bot.get("role") == "assistant"):
            pairs += [{"role": "user", "content": str(user.get("content", ""))[:MAX_MESSAGE_CHARS]},
                      {"role": "assistant", "content": str(bot.get("content", ""))[:8000]}]
    return pairs[-HISTORY_LIMIT:]


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body, ctype: str = "application/json; charset=utf-8") -> None:
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        if self.path in ("/", "/index.html"):
            self._send(200, PAGE.read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/api/info":
            self._send(200, {"backend": SESSION.backend, "model": SESSION.ollama.model,
                             "chunks": get_collection().count()})
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self) -> None:
        if self.path != "/api/chat":
            return self._send(404, {"error": "not found"})
        try:
            length = min(int(self.headers.get("Content-Length", 0)), 200_000)
            req = json.loads(self.rfile.read(length) or b"{}")
            message = str(req.get("message", "")).strip()[:MAX_MESSAGE_CHARS]
            if not message:
                return self._send(400, {"error": "empty message"})
            session = ChatSession(SESSION.backend, SESSION.ollama, history=parse_history(req.get("history")))
            turn = session.ask(message)
        except (ValueError, TypeError) as e:
            return self._send(400, {"error": f"bad request: {e}"})
        except Exception as e:  # report it to the page instead of dropping the connection
            return self._send(502, {"error": f"{type(e).__name__}: {e}"})
        self._send(200, {
            "answer": turn.answer,
            "route": turn.route.kind,
            "search_query": turn.route.search_query,
            "sources": [{"title": c.source_title, "edition": c.edition, "version": c.game_version}
                        for c in turn.chunks],
            "history": session.history,
        })

    def log_message(self, fmt, *args) -> None:  # keep the console quiet
        pass


def main() -> None:
    global SESSION
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="CraftGuide web chat")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--backend", default=BACKEND, choices=BACKEND_CHOICES,
                        help="auto uses Ollama when it is running and has the model, offline otherwise")
    parser.add_argument("--model", default=OLLAMA_MODEL, help="the Ollama model (default: %(default)s)")
    args = parser.parse_args()

    SESSION, status = open_session(args.backend, args.model)
    print(status)
    if get_collection().count() == 0:
        print("Building the vector database from data/ (first run only)...")
        ingest()
    print(f"{get_collection().count()} chunks. Open http://localhost:{args.port}  (Ctrl+C to stop)")
    try:
        ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
