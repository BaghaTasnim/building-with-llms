from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = []

print("Chat with AI! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break
    
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."}
        ] + conversation_history,
        temperature=0.7,
        max_tokens=500
    )
    
    ai_response = response.choices[0].message.content
    
    conversation_history.append({
        "role": "assistant",
        "content": ai_response
    })
    
    print(f"AI: {ai_response}\n")