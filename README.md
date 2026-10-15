# CraftGuide: a Minecraft RAG chatbot

CraftGuide answers Minecraft questions from the reference files in `data/`. It uses ChromaDB plus keyword search for retrieval and Claude for answers.
Without an API key it runs on its own in offline mode: it quotes the best-matching lines from the library, with sources.

## Setup

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env   # optional: put your Anthropic API key in .env for Claude answers
python ingest.py         # build the vector database
```

The first run of `ingest.py` downloads ChromaDB's default embedding model (about 80 MB).

## Use

```powershell
python server.py         # web chat at http://localhost:8000
python chat.py           # chat in the terminal
python chat.py --backend offline   # force offline mode even with an API key
python chat.py --debug   # also show each message's route, search query and retrieved sources
python test_session.py                    # offline checks of routing, history and /reset (fake Claude client)
python test_questions.py                  # end-to-end questions and conversations (needs the claude backend)
python test_questions.py --retrieval-only # retrieval checks only, no API key needed
```

Type `/reset` in the chat to clear the history, or `/quit` to exit.

## Backends

`BACKEND=auto` (the default) uses Claude when `ANTHROPIC_API_KEY` is set and offline mode otherwise. Override it with `--backend` or the `BACKEND` variable.

| | claude | offline |
|---|---|---|
| Needs | API key | nothing (after the one-time embedding model download) |
| Casual conversation | answered without retrieval, with the last 20 messages as memory | not supported: every message is searched |
| Follow-up questions | rewritten into standalone search queries | searched as typed |
| Answer | written by Claude from the retrieved chunks | the best-matching lines of the retrieved chunks (`offline.py`) |
| Off-topic questions | refused by the system prompt | refused when the question uses words the library doesn't contain |

## How it works

1. `ingest.py` reads every file in `data/` and splits it by `#`, `##`, and `###` headings. Sections longer than 700 characters are split further. A long table repeats its header row in each piece. Each chunk gets this metadata:
   - `source_title`: the heading path, for example `Mobs (Creatures) > Hostile mobs`.
   - `edition`: `Java` or `Bedrock` when the section mentions only that edition, otherwise `both`.
   - `game_version`: the newest version number the section mentions, or empty.
   - `file`: the first file the chunk was found in.

   The chunk ID is a hash of the title and text. `data/` contains the same sections several times (the per-topic files, `MINECRAFT_COMPLETE.md`, and `MINECRAFT_COMPLETE.txt`), so the duplicates collapse to one chunk. Rerunning `ingest.py` updates changed chunks and removes chunks whose source text is gone.
2. `rag.py` sends each message and the chat history to a small Claude model in one call. The model returns JSON with two fields:
   - `kind`: `minecraft` for Minecraft questions, including follow-ups. `chitchat` for everything else: greetings, small talk, personal facts, and requests unrelated to Minecraft.
   - `search_query`: for `minecraft`, a standalone search query with references resolved from the history.
3. For `minecraft`, retrieval runs two searches: ChromaDB vector search, and a keyword search (`offline.keyword_search`) that weights rare words more, so exact names such as `creeper` are not missed. Their rankings are merged with reciprocal rank fusion. The top 5 chunks are formatted with their source title, edition, and version. For `chitchat`, retrieval is skipped and the documents are `(no documents: casual conversation)`.
4. Offline mode has no router. It searches every message, and `offline.py` quotes the retrieved lines that best match the question words.
5. `server.py` serves the web chat in `web/index.html` using only the Python standard library. The page sends the conversation history with each message, so the server keeps no state, and **New chat** clears it.
6. The documents and the original message fill `{retrieved_documents}` and `{user_question}` in `prompts/system_prompt.md`. The prompt is otherwise used unchanged. The last 20 messages of the conversation (10 exchanges) are sent as prior messages, so the bot remembers what the user said earlier.

## Configuration

Set these in `.env`:

| Variable | Default | Purpose |
|---|---|---|
| `ANTHROPIC_API_KEY` | none | Enables the Claude backend. |
| `BACKEND` | `auto` | `auto`, `claude`, or `offline`. |
| `ANSWER_MODEL` | `claude-opus-5-5` | Writes the answers. |
| `ROUTER_MODEL` | `claude-haiku-5-5` | Classifies each message and rewrites Minecraft follow-ups into search queries. |
