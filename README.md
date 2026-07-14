# groq-cli-chatbot

A simple command-line chatbot built using the Groq API (Llama 3.3 70B).
Built as Day 1 of a 60-day GenAI Developer learning plan — raw API calls first, 
frameworks (LangChain, RAG, agents) added in later weeks.

## Features
- Menu-driven CLI interface
- Error handling for invalid input
- Environment variable based API key management

## Setup
1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it and run `pip install groq`
4. Set your API key: `$env:GROQ_API_KEY="your-key"` (PowerShell)
5. Run: `python py.py`
