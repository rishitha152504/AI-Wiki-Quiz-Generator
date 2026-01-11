# 🚀 Start Backend - Quick Guide

## Step 1: Start Backend Server

1. **Go to your QUIZ folder:**
   `C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ`

2. **Double-click:** `start-backend.bat`

3. **A black window will open** - this is your backend server

4. **Wait for this message:**
   ```
   Uvicorn running on http://0.0.0.0:8000
   Application startup complete.
   ```

5. **Keep this window open!** (Don't close it)

---

## Step 2: Verify Backend is Running

1. **Open a new browser tab**
2. **Go to:** http://localhost:8000/api/health
3. **You should see:**
   ```json
   {"status":"healthy","message":"Backend is running and ready","database":"connected"}
   ```

If you see this, backend is working! ✅

---

## Step 3: Test Connection in Frontend

1. **Go back to your frontend** (http://localhost:3000)
2. **Press F12** to open Developer Tools
3. **Click the "Console" tab**
4. **Look for:** `✅ Backend connection successful`

If you see this, frontend and backend are connected! ✅

---

## Step 4: Test the Full App

1. **In the frontend**, make sure you're on the "Generate Quiz" tab
2. **The URL should already be filled:** `https://en.wikipedia.org/wiki/Alan_Turing`
3. **Click "Generate Quiz" button**
4. **Wait about 30 seconds** (it needs to scrape Wikipedia and generate quiz)
5. **Quiz should appear!** 🎉

---

## ⚠️ Troubleshooting

### Backend won't start?

**Error: "GEMINI_API_KEY not set"**
- Check: `backend/.env` file exists
- Check: It contains `GEMINI_API_KEY=your_key_here`
- We already created this, so it should be fine!

**Error: "Port 8000 already in use"**
- Another program is using port 8000
- Close other programs
- Or restart your computer

**Backend starts but frontend can't connect?**
- Make sure backend window is still open
- Check: http://localhost:8000/api/health works in browser
- Check browser console (F12) for errors

---

## ✅ Success Checklist

- [ ] Backend window is open and shows "Uvicorn running"
- [ ] http://localhost:8000/api/health shows healthy status
- [ ] Frontend console shows "✅ Backend connection successful"
- [ ] Can generate a quiz successfully

---

**Ready? Double-click `start-backend.bat` now!** 🚀
