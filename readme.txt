CraftGuide - Minecraft chatbot
==============================

CraftGuide runs on your computer. After setup it needs no internet
connection and no account.

How to run the chat (Windows, PowerShell)
-----------------------------------------

1. First time only - install Ollama and the model:

   - Install Ollama from https://ollama.com/download
   - Download the model (about 2 GB):

       ollama pull qwen2.5:3b

2. First time only - open PowerShell in this folder (minecraft-rag-bot)
   and set up Python:

     python -m venv .venv
     .venv\Scripts\activate
     pip install -r requirements.txt
     python ingest.py

   - The first "python ingest.py" downloads an embedding model (about 80 MB).
     After that and the model download, everything runs offline.
   - Run "python ingest.py" again whenever you change the files in data\.

3. Every time - make sure Ollama is running (the Ollama app starts it when
   you sign in, or run "ollama serve" in another window). Then activate the
   environment and start the chat:

     .venv\Scripts\activate

   Web chat:
     python server.py
     then open http://localhost:8000 in your browser.
     Press Ctrl+C in PowerShell to stop the server.

   Terminal chat:
     python chat.py

   The first line the chat prints says which mode it is in, for example
   "CraftGuide: Ollama · qwen2.5:3b".

Offline mode
------------
If Ollama is not running or the model is not downloaded, CraftGuide starts
in offline mode and its first line says how to fix it. In offline mode it
answers greetings, thanks, goodbyes, "who are you", "my name is ..." and
"what's my name?", and answers Minecraft questions by quoting matching
lines from the files in data\. If Ollama stops while you chat, CraftGuide
answers in offline mode until Ollama is back.

Chat commands (terminal)
------------------------
  /reset   clear the conversation history
  /quit    exit

Useful options
--------------
  python chat.py --model llama3.2    use another Ollama model
                                     (download it first: ollama pull llama3.2)
  python chat.py --backend offline   use offline mode even when Ollama runs
  python chat.py --debug             show route, search query and sources

Settings (environment variables)
--------------------------------
  OLLAMA_MODEL   the model to use (default qwen2.5:3b)
  OLLAMA_URL     where Ollama listens (default http://localhost:11434)
  BACKEND        auto, ollama or offline (default auto)

Tests
-----
  python test_session.py                     checks with a fake Ollama, no network
  python test_questions.py --retrieval-only  retrieval checks, no Ollama needed
  python test_questions.py                   full checks, needs Ollama and the model

See README.md for how the bot works.
