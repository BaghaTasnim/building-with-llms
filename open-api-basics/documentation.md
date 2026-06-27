# Documentation — OpenAI API in Python (using Groq)

## Why this project?
Instead of using ChatGPT through the browser, this project shows how to call an AI model directly from Python using the Groq API (free alternative to OpenAI).

---

## Steps

### 1. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
**Why?** — Keeps project dependencies isolated from other Python projects on your machine.

---

### 2. Install Dependencies
```bash
pip install groq python-dotenv
```
**Why these libraries?**
- `groq` — official library to talk directly to Groq API from Python
- `python-dotenv` — loads the API key from `.env` file so we never expose secrets in our code

> ⚠️ **Note:** We first tried using the `openai` library with Groq, but it gave a 404 error:
> `The deployment could not be found on Vercel.`
> The fix was to use the official `groq` library instead, which works directly with Groq API without any issues.

---

### 3. Create .env
```
GROQ_API_KEY=your_api_key_here
```
**Why?** — So your secret API key never gets exposed in your code or uploaded to GitHub.

---

### 4. Create .gitignore
```
.env
venv/
```
**Why?** — Tells Git to ignore the `.env` file and `venv` folder so they are never pushed to GitHub. This protects your API key and avoids uploading unnecessary files.

---

### 5. Create .env.example
```
GROQ_API_KEY=your_api_key_here
```
**Why?** — So anyone who clones your project knows what environment variables they need, without exposing your real key.

---

### 6. The Code (main.py)
```python
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

user_input = input("Ask me anything: ")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ],
    temperature=0.7,
    max_tokens=200
)

print(response.choices[0].message.content)
```

**Why each part?**
- `load_dotenv()` — reads the `.env` file and loads the API key into memory
- `Groq()` — creates the client (connection between our code and Groq API)
- `model` — which AI model to use
- `system` — secret instructions that tell the model how to behave
- `user_input` — takes the question from the terminal instead of hardcoding it
- `response.choices[0].message.content` — extracts only the text answer from the response
- `temperature` — controls how random the response is (0.0 = always same answer, 1.5 = very creative)
- `max_tokens` — limits the length of the response

> ⚠️ **Note:** We first tried using `llama3-8b-8192` but it gave this error:
> `The model llama3-8b-8192 has been decommissioned and is no longer supported.`
> The fix was to use `llama-3.3-70b-versatile` instead ✅

---

### temperature
Controls randomness of the response. Range: 0.0 → 2.0

| Value | Behavior | Use case |
|---|---|---|
| `0.0` | Always same answer | Code, math, facts |
| `0.7` | Balanced ✅ | General conversation |
| `1.5+` | Very creative | Stories, poems |

---

### max_tokens
Limits how long the response can be.

| Value | Response length |
|---|---|
| `50` | Very short |
| `200` | Medium ✅ |
| `1000+` | Long/detailed |

> ⚠️ **Groq Free Tier Limits:**
> - 30 requests/minute
> - 6,000 tokens/minute
> - 1,000 requests/day
>
> Good enough for learning and testing ✅

---

### 7. Run
```bash
python main.py
```