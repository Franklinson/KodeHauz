# AI Moderated Chat Script (Gemini)

## Setup

1. **Get Gemini API Key:**
   - Go to https://makersuite.google.com/app/apikey
   - Create a new API key
   - Copy the key

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set API Key:**
   - Edit `.env` file and replace `your-gemini-api-key-here` with your actual key

## Usage

```bash
python ai_moderated_chat.py
```

Enter your prompt when prompted. The script will:
- Check input for banned keywords
- Send to Gemini API if safe
- Moderate the response
- Display the result

## Features

- Input moderation (blocks harmful prompts)
- Output moderation (redacts unsafe content)
- Google Gemini Pro integration
- Simple keyword-based filtering
- Error handling for API issues