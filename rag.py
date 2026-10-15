"""Retrieval-augmented answering: route the message, retrieve chunks, then answer.

Two backends, both local:
  * ollama  - a local model served by Ollama routes each message (Minecraft or chitchat), rewrites
              follow-ups into standalone search queries, and writes the answer.
  * offline - scripted small talk, otherwise searches the message and quotes the best-matching lines
              (offline.py).
BACKEND=auto (the default) uses Ollama when it is running and has OLLAMA_MODEL, offline otherwise.
"""

import http.client
import json
import os
import urllib.request
from dataclasses import dataclass, field
from typing import Callable, Literal

import offline
from ingest import ROOT, get_collection, ingest

SYSTEM_TEMPLATE = (ROOT / "prompts" / "system_prompt.md").read_text(encoding="utf-8")
Backend = Literal["ollama", "offline"]
BACKEND_CHOICES = ("auto", "ollama", "offline")
BACKEND = os.getenv("BACKEND", "auto")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
PING_TIMEOUT = 2
CHAT_TIMEOUT = 300  # a 3B model on CPU can take a minute per answer, longer while it loads
NUM_CTX = 8192      # Ollama's default window is smaller than the system prompt plus 5 chunks plus history
TOP_K = 5
CANDIDATES = 15  # per ranking, before fusion
RRF_K = 60       # the usual reciprocal rank fusion constant
HISTORY_LIMIT = 20  # messages (10 exchanges); even, so the window always starts with a user message
NO_DOCUMENTS = "(no documents: casual conversation)"

ROUTER_INSTRUCTIONS = """Classify the user's latest message for a Minecraft assistant.
- kind "minecraft": a question about Minecraft, including follow-ups to earlier Minecraft questions.
- kind "chitchat": anything else (greetings, small talk, personal facts, questions about the user or the \
conversation such as "what's my name?", requests unrelated to Minecraft).
For "minecraft", write search_query: a standalone search query for a Minecraft knowledge base, with \
pronouns and references resolved from the conversation. Use the user's own words and add nothing they \
didn't say. For "chitchat", search_query is an empty string."""

ROUTE_SCHEMA = {
    "type": "object",
    "properties": {
        "kind": {"type": "string", "enum": ["minecraft", "chitchat"]},
        "search_query": {"type": "string"},
    },
    "required": ["kind", "search_query"],
    "additionalProperties": False,
}


@dataclass(frozen=True)
class RetrievedChunk:
    source_title: str
    edition: str
    game_version: str
    text: str
    distance: float | None  # None for chunks found only by keyword search


@dataclass(frozen=True)
class Route:
    kind: Literal["minecraft", "chitchat"]
    search_query: str


@dataclass(frozen=True)
class Turn:
    question: str
    route: Route
    chunks: list[RetrievedChunk]
    answer: str


def retrieve(query: str, k: int = TOP_K) -> list[RetrievedChunk]:
    """Hybrid search: merge the vector and keyword rankings with reciprocal rank fusion."""
    collection = get_collection()
    if collection.count() == 0:
        ingest()
    result = collection.query(query_texts=[query], n_results=CANDIDATES)
    vector_ids = result["ids"][0]
    distances = dict(zip(vector_ids, result["distances"][0]))
    keyword_hits = {c.id: c for c in offline.keyword_search(query, CANDIDATES)}
    fused: dict[str, float] = {}
    for ranking in (vector_ids, list(keyword_hits)):
        for rank, chunk_id in enumerate(ranking):
            fused[chunk_id] = fused.get(chunk_id, 0.0) + 1 / (RRF_K + rank)
    best = sorted(fused, key=fused.get, reverse=True)[:k]

    # Stored documents start with the source title line; drop it so chunk.text is the body.
    docs = dict(zip(vector_ids, result["documents"][0]))
    metas = dict(zip(vector_ids, result["metadatas"][0]))
    chunks = []
    for chunk_id in best:
        if chunk_id in docs:
            meta, text = metas[chunk_id], docs[chunk_id].split("\n", 1)[-1]
        else:
            hit = keyword_hits[chunk_id]
            meta, text = hit.metadata, hit.text
        chunks.append(RetrievedChunk(meta["source_title"], meta["edition"], meta["game_version"], text,
                                     distances.get(chunk_id)))
    return chunks


def format_documents(chunks: list[RetrievedChunk]) -> str:
    if not chunks:
        return NO_DOCUMENTS
    return "\n\n".join(
        f'<document index="{i}">\n'
        f"Source title: {c.source_title}\n"
        f"Edition: {c.edition}\n"
        f"Game version: {c.game_version or 'unknown'}\n\n"
        f"{c.text}\n"
        f"</document>"
        for i, c in enumerate(chunks, 1)
    )


def build_system_prompt(chunks: list[RetrievedChunk], question: str) -> str:
    return (SYSTEM_TEMPLATE
            .replace("{retrieved_documents}", format_documents(chunks))
            .replace("{user_question}", question))


def parse_route(text: str, question: str) -> Route:
    """Read the router's JSON. Anything malformed falls back to searching the raw question."""
    try:
        data = json.loads(text)
        kind, query = data["kind"], str(data.get("search_query", "")).strip()
    except (ValueError, TypeError, KeyError):
        return Route("minecraft", question)
    if kind == "chitchat":
        return Route("chitchat", "")
    return Route("minecraft", query or question)


class OllamaUnavailable(Exception):
    """Ollama could not be reached or sent a reply that isn't the shape we expect."""


Transport = Callable[[str, dict | None], dict]  # (path, JSON body or None for a GET) -> JSON reply


def http_transport(url: str) -> Transport:
    def send(path: str, payload: dict | None) -> dict:
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(url.rstrip("/") + path, data=data,
                                         headers={"Content-Type": "application/json"})
        # The only GET is the startup ping, which must fail fast when Ollama isn't running.
        timeout = PING_TIMEOUT if payload is None else CHAT_TIMEOUT
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.load(response)
    return send


class Ollama:
    def __init__(self, model: str = OLLAMA_MODEL, url: str = OLLAMA_URL, transport: Transport | None = None):
        self.model, self.url = model, url
        self.transport = transport or http_transport(url)

    def _call(self, path: str, payload: dict | None) -> dict:
        try:
            reply = self.transport(path, payload)
        except (OSError, ValueError, http.client.HTTPException) as e:  # URLError, HTTPError, timeouts, bad JSON
            raise OllamaUnavailable(f"{type(e).__name__}: {e}") from e
        if not isinstance(reply, dict):
            raise OllamaUnavailable(f"unexpected reply from {path}: {reply!r:.200}")
        return reply

    def models(self) -> list[str]:
        reply = self._call("/api/tags", None)
        models = reply.get("models")
        if not isinstance(models, list):
            raise OllamaUnavailable(f"unexpected reply from /api/tags: {reply!r:.200}")
        return [m["name"] for m in models if isinstance(m, dict) and isinstance(m.get("name"), str)]

    def chat(self, messages: list[dict[str, str]], *, format: dict | None = None, temperature: float) -> str:
        payload = {"model": self.model, "messages": messages, "stream": False,
                   "options": {"temperature": temperature, "num_ctx": NUM_CTX}}
        if format is not None:
            payload["format"] = format
        reply = self._call("/api/chat", payload)
        message = reply.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, str):
            raise OllamaUnavailable(f"unexpected reply from /api/chat: {reply!r:.200}")
        return content.strip()


def resolve_backend(choice: str, ollama: Ollama) -> tuple[Backend, str]:
    """Pick the backend for this run, plus a startup line naming it (and, when offline, why and the fix)."""
    if choice not in BACKEND_CHOICES:
        raise SystemExit(f"BACKEND must be one of {', '.join(BACKEND_CHOICES)}, not {choice!r}")
    if choice == "offline":
        return "offline", "CraftGuide: offline mode (chosen with --backend offline)."
    model = ollama.model
    try:
        names = ollama.models()
    except OllamaUnavailable as e:
        return "offline", (f"CraftGuide: offline mode. Ollama isn't reachable at {ollama.url} ({e}). "
                           f"Start it with `ollama serve`, run `ollama pull {model}` once, then restart CraftGuide.")
    if model not in names and f"{model}:latest" not in names:
        return "offline", (f"CraftGuide: offline mode. Ollama is running but doesn't have {model}. "
                           f"Run `ollama pull {model}`, then restart CraftGuide.")
    return "ollama", f"CraftGuide: Ollama · {model}"


@dataclass
class ChatSession:
    backend: Backend
    ollama: Ollama
    history: list[dict[str, str]] = field(default_factory=list)

    def route(self, question: str) -> Route:
        transcript = "\n".join(f"{m['role'].title()}: {m['content']}" for m in self.history)
        reply = self.ollama.chat([
            {"role": "system", "content": ROUTER_INSTRUCTIONS},
            {"role": "user", "content": f"<conversation>\n{transcript}\n</conversation>\n\nLatest message: {question}"},
        ], format=ROUTE_SCHEMA, temperature=0)
        return parse_route(reply, question)

    def ask_ollama(self, question: str) -> Turn:
        route = self.route(question)
        chunks = retrieve(route.search_query) if route.kind == "minecraft" else []
        answer = self.ollama.chat([
            {"role": "system", "content": build_system_prompt(chunks, question)},
            *self.history,
            {"role": "user", "content": question},
        ], temperature=0.3)
        return Turn(question, route, chunks, answer)

    def ask_offline(self, question: str) -> Turn:
        reply = offline.small_talk(question, self.history)
        if reply is not None:
            return Turn(question, Route("chitchat", ""), [], reply)
        chunks = retrieve(question)
        return Turn(question, Route("minecraft", question), chunks, offline.answer(question, chunks))

    def ask(self, question: str) -> Turn:
        try:
            turn = self.ask_ollama(question) if self.backend == "ollama" else self.ask_offline(question)
        except OllamaUnavailable:  # Ollama stopped after startup: answer this turn offline
            turn = self.ask_offline(question)
        self.history += [{"role": "user", "content": question}, {"role": "assistant", "content": turn.answer}]
        del self.history[:-HISTORY_LIMIT]
        return turn


def open_session(choice: str = BACKEND, model: str = OLLAMA_MODEL) -> tuple[ChatSession, str]:
    """A session on the resolved backend, and the startup line to print."""
    ollama = Ollama(model)
    backend, status = resolve_backend(choice, ollama)
    return ChatSession(backend, ollama), status
