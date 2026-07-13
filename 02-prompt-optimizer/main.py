from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

user_prompt = input("Enter your prompt: ")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a prompt engineering expert. Your job is to take a simple prompt and rewrite it into a detailed, clear, and effective prompt that will get better results from an AI model."},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.7,
    max_tokens=500
)

optimized_prompt = response.choices[0].message.content
print("\nOptimized Prompt:")
print(optimized_prompt)
