"""Retrieval-augmented answering: route the message, retrieve chunks, then answer.

Two backends:
  * claude  - a small model routes each message (Minecraft or chitchat) and rewrites follow-ups into
              standalone search queries; a larger model writes the answer. Needs ANTHROPIC_API_KEY.
  * offline - searches every message and quotes the best-matching lines (offline.py). No API key needed.
BACKEND=auto (the default) uses Claude when an API key is set and offline otherwise.
"""

import json
import os
from dataclasses import dataclass, field
from typing import Any, Literal

from dotenv import load_dotenv

import offline
from ingest import ROOT, get_collection, ingest

load_dotenv(ROOT / ".env")

SYSTEM_TEMPLATE = (ROOT / "prompts" / "system_prompt.md").read_text(encoding="utf-8")
ANSWER_MODEL = os.getenv("ANSWER_MODEL", "claude-opus-5-5")
ROUTER_MODEL = os.getenv("ROUTER_MODEL", "claude-haiku-5-5")
BACKENDS = ("auto", "claude", "offline")
BACKEND = os.getenv("BACKEND", "auto")
TOP_K = 5
CANDIDATES = 15  # per ranking, before fusion
RRF_K = 60       # the usual reciprocal rank fusion constant
HISTORY_LIMIT = 20  # messages (10 exchanges); even, so the window always starts with a user message
NO_DOCUMENTS = "(no documents: casual conversation)"

ROUTER_INSTRUCTIONS = """Classify the user's latest message for a Minecraft assistant.
- kind "minecraft": a question about Minecraft, including follow-ups to earlier Minecraft questions.
- kind "chitchat": anything else (greetings, small talk, personal facts, requests unrelated to Minecraft).
For "minecraft", write search_query: a standalone search query for a Minecraft knowledge base, with \
pronouns and references resolved from the conversation, keeping the edition (Java/Bedrock) if one was \
mentioned. For "chitchat", search_query is an empty string."""

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


def resolve_backend(backend: str = BACKEND) -> str:
    if backend not in BACKENDS:
        raise SystemExit(f"BACKEND must be one of {', '.join(BACKENDS)}, not {backend!r}")
    if backend == "auto":
        key = os.getenv("ANTHROPIC_API_KEY", "")
        has_sdk = True
        try:
            import anthropic  # noqa: F401
        except ImportError:
            has_sdk = False
        return "claude" if has_sdk and key and key != "your-api-key-here" else "offline"
    return backend


def make_client() -> Any:
    try:
        import anthropic
    except ImportError:
        raise SystemExit("The claude backend needs the SDK: pip install anthropic") from None
    return anthropic.Anthropic()


def text_of(response: Any) -> str:
    return "".join(block.text for block in response.content if block.type == "text").strip()


@dataclass
class ChatSession:
    backend: str = field(default_factory=resolve_backend)
    client: Any = None
    history: list[dict[str, str]] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.backend = resolve_backend(self.backend)
        if self.backend == "claude" and self.client is None:
            self.client = make_client()

    def route(self, question: str) -> Route:
        if self.backend == "offline":
            return Route("minecraft", question)
        transcript = "\n".join(f"{m['role'].title()}: {m['content']}" for m in self.history)
        response = self.client.messages.create(
            model=ROUTER_MODEL,
            max_tokens=1024,
            system=ROUTER_INSTRUCTIONS,
            output_config={"effort": "low", "format": {"type": "json_schema", "schema": ROUTE_SCHEMA}},
            messages=[{
                "role": "user",
                "content": f"<conversation>\n{transcript}\n</conversation>\n\nLatest message: {question}",
            }],
        )
        return parse_route(text_of(response), question)

    def answer(self, question: str, chunks: list[RetrievedChunk]) -> str:
        if self.backend == "offline":
            return offline.answer(question, chunks)
        response = self.client.messages.create(
            model=ANSWER_MODEL,
            max_tokens=16000,
            system=build_system_prompt(chunks, question),
            messages=[*self.history, {"role": "user", "content": question}],
        )
        if getattr(response, "stop_reason", None) == "refusal":
            return "Sorry, I can't help with that one. Ask me something else about Minecraft!"
        return text_of(response)

    def ask(self, question: str) -> Turn:
        route = self.route(question)
        chunks = retrieve(route.search_query) if route.kind == "minecraft" else []
        turn = Turn(question, route, chunks, self.answer(question, chunks))
        self.history += [{"role": "user", "content": question}, {"role": "assistant", "content": turn.answer}]
        del self.history[:-HISTORY_LIMIT]
        return turn
