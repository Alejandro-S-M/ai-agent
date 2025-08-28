# ai-agent

import os
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types

def main():
    print("Hello from ai-agent!")
    ok = load_dotenv() 
    print("Setup status:", "dotenv loaded =", ok)
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    print("API key present:", bool(api_key))
    client = genai.Client(api_key=api_key)
    
    # User input with sys.argv
    args = sys.argv[1:]
    verbose_flag = "--verbose" in args
    prompt_args = [arg for arg in args if arg != "--verbose"]
    
    # Check for verbose flag and uotuput reponse
    if not prompt_args:
        print("Error: prompt not provided")
        return

    user_prompt = prompt_args[0]

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    if verbose_flag:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print("User prompt:", user_prompt)
        print("Prompt tokens:", prompt_tokens)
        print("Response tokens:", response_tokens)

    print(response.text)

if __name__ == "__main__":
    main()

