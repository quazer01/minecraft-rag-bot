CraftGuide - Minecraft chatbot
==============================

How to run the chat (Windows, PowerShell)
-----------------------------------------

1. Open PowerShell in this folder (minecraft-rag-bot).

2. First time only - set up:

     python -m venv .venv
     .venv\Scripts\activate
     pip install -r requirements.txt
     copy .env.example .env
     python ingest.py

   - Optional: open .env and set ANTHROPIC_API_KEY=your-key to get answers
     written by Claude. Without a key the bot runs in offline mode and
     quotes matching lines from the files in data\.
   - The first "python ingest.py" downloads an embedding model (about 80 MB).
   - Run "python ingest.py" again whenever you change the files in data\.

3. Every time - activate the environment, then start the chat:

     .venv\Scripts\activate

   Web chat:
     python server.py
     then open http://localhost:8000 in your browser.
     Press Ctrl+C in PowerShell to stop the server.

   Terminal chat:
     python chat.py

Chat commands (terminal)
------------------------
  /reset   clear the conversation history
  /quit    exit

Useful options
--------------
  python chat.py --backend offline   force offline mode even with an API key
  python chat.py --debug             show route, search query and sources

Tests
-----
  python test_session.py                     offline checks, no API key needed
  python test_questions.py --retrieval-only  retrieval checks, no API key needed
  python test_questions.py                   full checks, needs an API key

See README.md for how the bot works and all settings.
