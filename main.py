# python

import os
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types

def main():
    print("Hello from ai-agent!")
    ok = load_dotenv() 
    print("Setup status:")
    print("dotenv loaded:", ok)
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    print("API key present:", bool(api_key))
    client = genai.Client(api_key=api_key)
    
    # Get user input
    user_prompt = input("Enter a prompt: ")
    
    # Validate input
    if not user_prompt:
        print("Error: prompt not provided")
        exit()    
    
    # Create messages list
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Output response
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages, 
    )
    print("Prompt tokens:",  response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()

