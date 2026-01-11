# Gemini API Quota & Rate Limits Guide

## Understanding the Error

When you see "API quota exceeded", it means you've hit one of Google's API limits.

## Free Tier Limits

### Rate Limits (Per Minute):
- **60 requests per minute** (RPM)
- **1,500 requests per day** (RPD)

### Token Limits:
- **1 million tokens per minute** (TPM)
- **32,000 tokens per request**

## Solutions

### 1. Wait and Retry
- **Wait 1-2 minutes** before trying again
- Rate limits reset every minute
- Daily limits reset at midnight (Pacific Time)

### 2. Check Your Usage
1. Go to: https://aistudio.google.com/app/apikey
2. Sign in with your Google account
3. View your API usage and quotas
4. Check if you've exceeded limits

### 3. Use Cached Quizzes
- The app caches quizzes in the database
- If you've generated a quiz for a URL before, it won't use the API
- Check the "Past Quizzes" tab to see cached quizzes

### 4. Reduce API Usage
- **Reuse existing quizzes**: Check history before generating new ones
- **Wait between requests**: Don't generate multiple quizzes rapidly
- **Use shorter articles**: Longer articles use more tokens

### 5. Upgrade Your Plan (If Needed)
- Free tier is generous for development
- For production, consider upgrading:
  - Go to Google Cloud Console
  - Enable billing (if needed)
  - Higher quotas available

## Best Practices

1. **Cache First**: Always check if a quiz exists before generating
2. **Batch Requests**: If generating multiple quizzes, space them out
3. **Monitor Usage**: Check your API dashboard regularly
4. **Error Handling**: The app now shows helpful error messages

## Checking Current Usage

Run this to see your API status:
```python
# In Python
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# This will show if your API key is valid
try:
    model = genai.GenerativeModel('gemini-2.0-flash-001')
    response = model.generate_content("Test")
    print("API is working!")
except Exception as e:
    print(f"API Error: {e}")
```

## When Limits Reset

- **Per-minute limits**: Reset every 60 seconds
- **Daily limits**: Reset at midnight Pacific Time (UTC-8)
- **Monthly limits**: Reset on the 1st of each month

## Need Help?

- Check Google's documentation: https://ai.google.dev/docs/quota
- View your quotas: https://aistudio.google.com/app/apikey
- Contact Google Cloud Support if you need higher limits
