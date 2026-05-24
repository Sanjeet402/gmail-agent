# Gmail AI Agent

A simple AI agent that connects to Gmail using LangGraph + Groq.

## Features
- Search unread Gmail emails
- Summarize emails
- Create draft emails
- Interactive command-line chat agent

## Tech Stack
- Python
- LangGraph
- LangChain
- Groq
- Gmail API
- OAuth 2.0

## Setup

### Clone
git clone <repo-url>

### Create venv
python -m venv venv

### Activate
venv\Scripts\activate

### Install
pip install -r requirements.txt

### Environment
Create `.env`

GROQ_API_KEY=your_key

### Google OAuth
Download `credentials.json` from Google Cloud Console and place in project root.

### Run
python agent.py
