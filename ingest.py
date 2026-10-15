"""Split the Minecraft reference files into heading sections and store them in ChromaDB."""

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import chromadb

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
DB_DIR = ROOT / "chroma_db"
COLLECTION = "minecraft"
MAX_CHUNK_CHARS = 700

Edition = Literal["Java", "Bedrock", "both"]

HEADING = re.compile(r"^(#{1,3})\s+(.*\S)\s*$")
FILE_NUMBER = re.compile(r"^\d+\s*[—-]\s*")
# Two-part "1.x" numbers double as stats in the tables (attack speed 1.6), so they
# only count as versions after a version-ish lead-in.
VERSION = re.compile(
    r"(?<![\d.])("
    r"1\.\d{1,2}\.\d{1,2}"
    r"|2[5-9]\.\d{1,2}"
    r"|(?:(?<=\()|(?<=since )|(?<=Java )|(?<=Bedrock )|(?<=release )|(?<=^\| )|(?<=^- ))1\.\d{1,2}"
    r")(?![\d.]*\d)",
    re.MULTILINE,
)


@dataclass(frozen=True)
class Chunk:
    text: str
    source_title: str
    edition: Edition
    game_version: str | None
    file: str

    @property
    def id(self) -> str:
        # The same section appears in several files (per-topic files and the merged
        # MINECRAFT_COMPLETE copies); hashing the content collapses those duplicates.
        return hashlib.sha1(f"{self.source_title}\n{self.text}".encode()).hexdigest()

    @property
    def metadata(self) -> dict[str, str]:
        return {
            "source_title": self.source_title,
            "edition": self.edition,
            "game_version": self.game_version or "",
            "file": self.file,
        }


def detect_edition(text: str) -> Edition:
    lowered = text.lower()
    java, bedrock = "java" in lowered, "bedrock" in lowered
    if java and not bedrock:
        return "Java"
    if bedrock and not java:
        return "Bedrock"
    return "both"


def detect_version(text: str) -> str | None:
    """Return the newest game version mentioned in the text, if any."""
    versions = VERSION.findall(text)
    if not versions:
        return None
    return max(versions, key=lambda v: tuple(int(part) for part in v.split(".")))


def split_blocks(body: str) -> list[str]:
    """Split on blank lines, keeping fenced code blocks whole."""
    blocks, current, in_fence = [], [], False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
        if not line.strip() and not in_fence:
            if current:
                blocks.append("\n".join(current))
                current = []
            continue
        current.append(line)
    if current:
        blocks.append("\n".join(current))
    return blocks


def split_oversized(block: str) -> list[str]:
    """Break a long block into row groups, repeating a table header in each group."""
    lines = block.splitlines()
    is_table = len(lines) > 2 and lines[0].startswith("|") and set(lines[1]) <= set("|-: ")
    header, rows = (lines[:2], lines[2:]) if is_table else ([], lines)
    groups, current = [], list(header)
    for row in rows:
        if len("\n".join(current + [row])) > MAX_CHUNK_CHARS and len(current) > len(header):
            groups.append("\n".join(current))
            current = list(header)
        current.append(row)
    groups.append("\n".join(current))
    return groups


def pack(body: str) -> list[str]:
    pieces = [p for block in split_blocks(body) for p in
              (split_oversized(block) if len(block) > MAX_CHUNK_CHARS else [block])]
    packed, current = [], ""
    for piece in pieces:
        if current and len(current) + len(piece) + 2 > MAX_CHUNK_CHARS:
            packed.append(current)
            current = piece
        else:
            current = f"{current}\n\n{piece}" if current else piece
    if current:
        packed.append(current)
    return packed


def chunk_file(path: Path) -> list[Chunk]:
    rel = path.relative_to(ROOT).as_posix()
    headings: dict[int, str] = {}
    sections: list[tuple[str, list[str]]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = HEADING.match(line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip("*")
            headings = {lvl: t for lvl, t in headings.items() if lvl < level}
            headings[level] = FILE_NUMBER.sub("", title) if level == 1 else title
            sections.append((" > ".join(headings[lvl] for lvl in sorted(headings)), []))
        elif sections:
            sections[-1][1].append(line)
        else:
            sections.append((path.stem, [line]))

    chunks = []
    for source_title, lines in sections:
        for text in pack("\n".join(lines).strip()):
            labelled = f"{source_title}\n{text}"
            chunks.append(Chunk(
                text=text,
                source_title=source_title,
                edition=detect_edition(labelled),
                game_version=detect_version(labelled),
                file=rel,
            ))
    return chunks


def load_chunks(data_dir: Path = DATA_DIR) -> list[Chunk]:
    unique: dict[str, Chunk] = {}
    for path in sorted(p for p in data_dir.rglob("*") if p.is_file()):
        for chunk in chunk_file(path):
            unique.setdefault(chunk.id, chunk)
    return list(unique.values())


def get_collection() -> chromadb.Collection:
    return chromadb.PersistentClient(path=str(DB_DIR)).get_or_create_collection(COLLECTION)


def ingest() -> int:
    """Sync the collection to the current data/ contents. Safe to rerun."""
    chunks = load_chunks()
    collection = get_collection()
    ids = [c.id for c in chunks]
    stale = set(collection.get(include=[])["ids"]) - set(ids)
    if stale:
        collection.delete(ids=list(stale))
    for start in range(0, len(chunks), 100):
        batch = chunks[start:start + 100]
        collection.upsert(
            ids=[c.id for c in batch],
            documents=[f"{c.source_title}\n{c.text}" for c in batch],
            metadatas=[c.metadata for c in batch],
        )
    return len(chunks)


if __name__ == "__main__":
    print(f"Stored {ingest()} unique chunks from {DATA_DIR} in {DB_DIR}")
