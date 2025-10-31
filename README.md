# AI Moderated Chat Script

## Setup

1. **Get OpenAI API Key:**
   - Sign up at https://platform.openai.com/
   - Create an API key in your account settings
   - Add billing information (required for API usage)

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variable:**
   ```bash
   OPENAI_API_KEY="your-api-key-here"
   ```

## Usage

```bash
python ai_moderated_chat.py
```

Enter your prompt when prompted. The script will:
- Check input for banned keywords
- Send to OpenAI API if safe
- Moderate the response
- Display the result

## Features

- Input moderation (blocks harmful prompts)
- Output moderation (redacts unsafe content)
- Simple keyword-based filtering
- Error handling for API issues