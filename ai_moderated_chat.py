#!/usr/bin/env python3
import openai
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
BANNED_KEYWORDS = ["kill", "hack", "bomb", "murder", "violence", "attack"]
SYSTEM_PROMPT = "You are a helpful, harmless, and honest AI assistant. Provide informative and safe responses."

def moderate_input(text):
    """Check if input contains banned keywords"""
    return any(keyword in text.lower() for keyword in BANNED_KEYWORDS)

def moderate_output(text):
    """Replace banned keywords in output with [REDACTED]"""
    moderated = text
    for keyword in BANNED_KEYWORDS:
        moderated = moderated.replace(keyword, "[REDACTED]")
        moderated = moderated.replace(keyword.capitalize(), "[REDACTED]")
        moderated = moderated.replace(keyword.upper(), "[REDACTED]")
    return moderated

def call_openai_api(user_prompt):
    """Make API call to OpenAI"""
    try:
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"API Error: {str(e)}"

def main():
    # Get API key
    if not os.getenv('OPENAI_API_KEY'):
        print("Please set OPENAI_API_KEY environment variable")
        sys.exit(1)
    
    # Get user input
    user_prompt = input("Enter your prompt: ").strip()
    
    if not user_prompt:
        print("Empty prompt provided")
        return
    
    # Input moderation
    if moderate_input(user_prompt):
        print("Your input violated the moderation policy.")
        return
    
    # API call
    ai_response = call_openai_api(user_prompt)
    
    # Output moderation
    if any(keyword in ai_response.lower() for keyword in BANNED_KEYWORDS):
        ai_response = moderate_output(ai_response)
    
    print(f"\nAI Response: {ai_response}")

if __name__ == "__main__":
    main()