# Quick Fix: API Key Error

## The Problem
You're seeing: "API key not valid" error

## The Solution (2 minutes)

### Step 1: Get Your Free API Key
1. Go to: **https://makersuite.google.com/app/apikey**
2. Sign in with Google
3. Click "Create API Key"
4. Copy the key (starts with `AIzaSy...`)

### Step 2: Update .env File
1. Open: `C:\Users\DELL\Desktop\QUIZ\backend\.env`
2. Find this line:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
3. Replace it with:
   ```
   GEMINI_API_KEY=AIzaSyYourActualKeyHere
   ```
4. Save the file

### Step 3: Restart Backend
1. Stop the server (press Ctrl+C in the terminal)
2. Start it again:
   ```powershell
   cd C:\Users\DELL\Desktop\QUIZ\backend
   python run.py
   ```

### Step 4: Try Again
Go back to the web app and try generating a quiz!

## That's It! 🎉

Your app should now work. The API key is free and no credit card is required.
