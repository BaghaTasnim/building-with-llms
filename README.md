## Project Source
https://roadmap.sh/projects/openai-api-python

# OpenAI API in Python

Call OpenAI models directly from Python, beyond the ChatGPT interface.

> ⚠️ This project uses **Groq** (free) instead of OpenAI API.

## Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install groq python-dotenv
```

### 3. Set Up API Key
1. Go to [console.groq.com](https://console.groq.com) and create an account
2. Generate an API key
3. Create a `.env` file:
```
GROQ_API_KEY=your_api_key_here
```

### 4. Run
```bash
python main.py
```

## What it does
A simple Python script that connects to Groq API and sends a prompt, then prints the response in the terminal.