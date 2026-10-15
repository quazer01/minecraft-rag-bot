"""Word matching with no language model and no API key: keyword search and offline answers.

Quotes the lines of the retrieved chunks that share the most words with the question, each with its
[Source: ...] title. Table rows are quoted under their header row so the columns stay readable.
A question is refused when most of its words never appear anywhere in the library, because vector
search always returns its nearest chunks, even for "What is the capital of France?".
"""

import math
import re
from collections import Counter
from functools import cache

from ingest import Chunk, load_chunks

TOKEN = re.compile(r"[a-z0-9]+")
STOPWORDS = set("""
a an and are as at be been but by can could did do does for from get got had has have how i if in into is it its
me my no not of on or our should so than that the their them then there these they this to too up was we were what
when where which who why will with would you your about any some all also just much many more most very
tell know want like please give show find make need hi hello hey thanks thank ok okay yes
""".split())
MAX_LINES = 6
NOT_FOUND = ("I couldn't find that in my Minecraft knowledge base. I'm running offline, so I can only quote "
             "the library: try asking about crafting, mobs, biomes, redstone, enchanting or commands.")
GREETING = ("Hi! I'm CraftGuide, running offline, so I can't chat, but I can look things up in my Minecraft "
            "library. Try \"how do I craft a bed?\" or \"how much health does an Enderman have?\"")


def stem(word: str) -> str:
    for suffix, replacement in (("ies", "y"), ("es", ""), ("s", "")):
        if len(word) > len(suffix) + 2 and word.endswith(suffix):
            return word[: -len(suffix)] + replacement
    return word


def terms(text: str) -> set[str]:
    return {stem(t) for t in TOKEN.findall(text.lower()) if t not in STOPWORDS and len(t) > 1}


@cache
def library() -> list[tuple[Chunk, frozenset[str]]]:
    return [(chunk, frozenset(terms(f"{chunk.source_title}\n{chunk.text}"))) for chunk in load_chunks()]


@cache
def library_idf() -> dict[str, float]:
    """Inverse document frequency of every library word: rare words ("teleport") outweigh common ones ("player")."""
    chunks = library()
    df = Counter(t for _, chunk_terms in chunks for t in chunk_terms)
    return {t: math.log(1 + len(chunks) / f) for t, f in df.items()}


def keyword_search(query: str, k: int) -> list[Chunk]:
    """Chunks containing the query's rarest words. Catches exact names ("creeper") that embeddings miss."""
    idf, wanted = library_idf(), terms(query)
    scored = [(sum(idf[t] for t in wanted & chunk_terms) / (1 + 0.002 * len(chunk.text)), i)
              for i, (chunk, chunk_terms) in enumerate(library())]
    scored = sorted((s for s in scored if s[0] > 0), reverse=True)[:k]
    return [library()[i][0] for _, i in scored]


def is_table_row(line: str) -> bool:
    return line.startswith("|")


def is_separator(line: str) -> bool:
    return is_table_row(line) and set(line) <= set("|-: ")


def answer(question: str, chunks) -> str:
    wanted = terms(question)
    if not wanted:
        return GREETING
    idf = library_idf()
    known = {t for t in wanted if t in idf}
    if len(known) < len(wanted) / 2:
        return NOT_FOUND

    # Score every line of every chunk, keeping the chunk order as a tie-breaker (better hits come first).
    scored = []
    for rank, chunk in enumerate(chunks):
        title_terms = terms(chunk.source_title)
        header = None
        for line in chunk.text.splitlines():
            line = line.strip()
            if not line or is_separator(line):
                continue
            if is_table_row(line) and header is None:
                header = line
                continue
            if not is_table_row(line):
                header = None
            line_terms = terms(line)
            if not known & line_terms:
                continue
            # Words in the line count fully, words only in the heading count half; long lines are penalised.
            weight = sum(idf[t] for t in known & line_terms) + 0.5 * sum(idf[t] for t in known & title_terms - line_terms)
            scored.append((weight / (1 + 0.01 * len(line.split())), rank, chunk.source_title, header, line))
    if not scored:
        return NOT_FOUND
    scored.sort(key=lambda s: (-s[0], s[1]))
    best, seen, picks = scored[0][0], set(), []
    for s in scored:
        if s[0] >= 0.6 * best and s[4] not in seen and len(picks) < MAX_LINES:
            seen.add(s[4])   # the same line can appear in overlapping chunks
            picks.append(s)

    # Group the picked lines by source, in order of first appearance.
    groups: dict[str, list[tuple[str | None, str]]] = {}
    for _, _, title, header, line in picks:
        groups.setdefault(title, []).append((header, line))
    parts = []
    for title, lines in groups.items():
        out, shown_header = [], None
        for header, line in lines:
            if header and header != shown_header:
                out += [header, "|" + "---|" * (header.count("|") - 1)]
                shown_header = header
            out.append(line if is_table_row(line) else f"- {line.lstrip('-* ')}")
        parts.append("\n".join(out) + f"\n[Source: {title}]")
    return "Here's what my Minecraft library says (offline mode):\n\n" + "\n\n".join(parts)
