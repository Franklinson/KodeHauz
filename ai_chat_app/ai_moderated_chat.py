#!/usr/bin/env python3
import google.generativeai as genai
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

def call_gemini_api(user_prompt):
    """Make API call to Google Gemini"""
    try:
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        
        # Use a known working model from your list
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_prompt}"
        response = model.generate_content(full_prompt)
        
        return response.text
    except Exception as e:
        return f"API Error: {str(e)}"

def main():
    # Get API key
    if not os.getenv('GEMINI_API_KEY'):
        print("Please set GEMINI_API_KEY environment variable")
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
    ai_response = call_gemini_api(user_prompt)
    
    # Output moderation
    if any(keyword in ai_response.lower() for keyword in BANNED_KEYWORDS):
        ai_response = moderate_output(ai_response)
    
    print(f"\nAI Response: {ai_response}")

if __name__ == "__main__":
    main()