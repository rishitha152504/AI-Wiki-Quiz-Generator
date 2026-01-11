# How to Get Your Gemini API Key

## Step-by-Step Instructions

### 1. Visit Google AI Studio
Go to: **https://makersuite.google.com/app/apikey**

### 2. Sign In
- Sign in with your Google account
- If you don't have a Google account, create one (it's free)

### 3. Create API Key
- Click "Create API Key" or "Get API Key"
- Select "Create API key in new project" (or use existing project)
- Your API key will be generated

### 4. Copy the API Key
- Copy the generated API key (it looks like: `AIzaSy...`)

### 5. Update .env File
1. Open `backend/.env` file in a text editor
2. Find the line: `GEMINI_API_KEY=your_gemini_api_key_here`
3. Replace `your_gemini_api_key_here` with your actual API key
4. Save the file

Example:
```
GEMINI_API_KEY=AIzaSyAbCdEfGhIjKlMnOpQrStUvWxYz1234567
```

### 6. Restart Backend Server
- Stop the backend server (Ctrl+C)
- Start it again: `python run.py`

## Important Notes

- ✅ **Free Tier Available**: Google Gemini API has a free tier with generous limits
- ✅ **No Credit Card Required**: For free tier usage
- 🔒 **Keep Your Key Secret**: Never share your API key or commit it to version control
- 📝 **Rate Limits**: Free tier has rate limits, but sufficient for development

## Troubleshooting

### Error: "API key not valid"
- Make sure you copied the entire key (no spaces before/after)
- Verify the key starts with `AIzaSy`
- Check that you saved the .env file
- Restart the backend server after updating .env

### Error: "Quota exceeded"
- You've hit the free tier limit
- Wait a bit and try again, or check your usage at Google AI Studio

### Can't find the API key page?
- Direct link: https://aistudio.google.com/app/apikey
- Or search: "Google AI Studio API key"
