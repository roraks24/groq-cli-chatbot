# groq-cli-chatbot

A command-line chatbot built on the Groq API (Llama 3.3 70B), built as Week 1 of a 60-day GenAI Developer learning plan. Started as a raw API call and grew into a persistent, persona-driven assistant with real error handling — every layer built and debugged from scratch.

## Features

- **Multi-turn conversation** — the model remembers earlier messages within a session by maintaining a running `conversation_history` list.
- **Persistent memory across runs** — conversation history is saved to `conversation_history.json` and reloaded automatically the next time the program starts.
- **API error handling** — gracefully catches `RateLimitError`, `APIConnectionError`, and `APIStatusError` instead of crashing, with clean messages and no corrupted history state.
- **Coding mentor persona** — a system prompt shapes the assistant into a coding mentor that gives roadmaps and explains bugs conceptually, without handing over full solutions or rewriting code directly.

## Setup

1. Clone the repo:
   ```
   git clone https://github.com/roraks24/groq-cli-chatbot.git
   cd groq-cli-chatbot
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\Activate     # Windows PowerShell
   ```

3. Install dependencies:
   ```
   pip install groq python-dotenv
   ```

4. Create a `.env` file in the project root with your Groq API key:
   ```
   GROQ_API_KEY=your_key_here
   ```

5. Run it:
   ```
   python py.py
   ```

## Usage

- Choose option `1` to start chatting.
- Type your message and press Enter.
- Type `#` to end the chat and return to the menu (this is also when conversation history is saved).
- Choose option `2` to quit the program.

## Known limitations

- **History is only saved on exit.** If the program is closed abruptly (force-quit, crash, closing the terminal directly) without typing `#` first, that session's messages are lost. History is not auto-saved after every message.
- **The persona doesn't enforce topic boundaries.** The system prompt defines *how* the assistant should behave on coding topics, but doesn't restrict it from answering unrelated questions (confirmed via real user testing — it happily answered a general knowledge and current-events question in Hindi). A stricter prompt or explicit refusal instruction would be needed to fix this.

## Built as part of

Week 1 of a 60-day GenAI Developer learning plan — raw API fundamentals before moving into LangChain, RAG, and agents in later weeks.
