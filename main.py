import os
from groq import Groq


#BCDE
#  API key here
API_KEY = "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"  

# Initialize Groq client
client = Groq(api_key=API_KEY)

def ask_groq(question):
    """Send a question to the Groq API and return the response."""
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": question}],
        max_tokens=100
    )
    
    # Extract the AI response correctly
    if response.choices:
        return response.choices[0].message.content.strip()
    else:
        return "No response from AI."

def main():
    print("Welcome to Groq Chatbot! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        
        answer = ask_groq(user_input)
        print(f"Groq: {answer}")

if __name__ == "__main__":
    main()
