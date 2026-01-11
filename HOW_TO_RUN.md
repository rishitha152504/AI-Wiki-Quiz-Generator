# 🚀 HOW TO RUN - Step by Step Guide

## 📍 Important: Run Scripts from Project Root

**Your project is located at:**
```
C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ
```

**You MUST run the scripts from this directory!**

---

## ✅ Step-by-Step Instructions

### Step 1: Open Project Folder

1. Open File Explorer
2. Navigate to: `C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ`
3. You should see these files:
   - `start-backend.bat`
   - `start-frontend.bat`
   - `backend/` folder
   - `frontend/` folder

### Step 2: Create Backend Configuration File

**⚠️ REQUIRED - Do this first!**

1. Open the `backend` folder
2. Create a new file named `.env` (not `.env.txt` - just `.env`)
3. Open `.env` in Notepad
4. Add this line:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
5. Replace `your_api_key_here` with your actual API key
6. Get API key from: https://makersuite.google.com/app/apikey
7. Save the file

**Example `.env` file content:**
```
GEMINI_API_KEY=AIzaSyAbc123xyz789...
```

### Step 3: Start Backend Server

1. **Double-click** `start-backend.bat` in the QUIZ folder
2. A black window (Command Prompt) will open
3. Wait for these messages:
   ```
   Starting Wiki Quiz Backend Server...
   Installing/updating dependencies...
   Starting FastAPI server on http://localhost:8000
   Uvicorn running on http://0.0.0.0:8000
   ```
4. **Keep this window open!** (Don't close it)

**If you see an error about `.env` file:**
- Go back to Step 2 and create the `.env` file

**If you see "port already in use":**
- Close any other programs using port 8000
- Or restart your computer

### Step 4: Start Frontend (New Window)

1. **Open a NEW File Explorer window**
2. Navigate to the QUIZ folder again
3. **Double-click** `start-frontend.bat`
4. A new Command Prompt window will open
5. Wait for:
   ```
   Starting Wiki Quiz Frontend...
   Starting React development server...
   ```
6. Your browser should open automatically at `http://localhost:3000`
7. **Keep this window open too!**

**If browser doesn't open:**
- Manually open: http://localhost:3000

### Step 5: Verify Connection

1. Open browser: http://localhost:3000
2. Press **F12** to open Developer Tools
3. Click the **Console** tab
4. Look for: `✅ Backend connection successful`

**If you see an error:**
- Make sure backend is still running (Step 3)
- Check backend window for errors
- Try refreshing the page (F5)

### Step 6: Test the App!

1. In the browser, go to "Generate Quiz" tab
2. Enter this URL: `https://en.wikipedia.org/wiki/Alan_Turing`
3. Click "Generate Quiz"
4. Wait about 30 seconds
5. Quiz should appear! 🎉

---

## 🔧 Alternative: Manual Method

If the scripts don't work, use these commands:

### Open PowerShell in QUIZ folder:

**Backend:**
```powershell
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
.\venv\Scripts\activate
python run.py
```

**Frontend (new PowerShell window):**
```powershell
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\frontend"
npm start
```

---

## ❌ Common Errors & Fixes

### Error: "Cannot find backend directory"
**Fix:** Make sure you're running the script from the QUIZ folder, not from inside backend or frontend folders

### Error: "GEMINI_API_KEY not set"
**Fix:** Create `backend/.env` file with your API key (see Step 2)

### Error: "Port 8000 already in use"
**Fix:** 
1. Close other programs using port 8000
2. Or restart computer
3. Or change port in `backend/run.py` (line 7) to 8001

### Error: "Cannot connect to backend"
**Fix:**
1. Make sure backend is running (Step 3)
2. Check backend window for errors
3. Test: Open http://localhost:8000/api/health in browser

### Frontend shows blank page
**Fix:**
1. Check browser console (F12) for errors
2. Make sure backend is running
3. Try refreshing (F5)

---

## 📋 Quick Checklist

Before starting:
- [ ] You're in the QUIZ folder
- [ ] `backend/.env` file exists with `GEMINI_API_KEY=...`
- [ ] Python is installed
- [ ] Node.js is installed

To run:
- [ ] Backend window is open and running
- [ ] Frontend window is open and running
- [ ] Browser shows http://localhost:3000
- [ ] Console shows "✅ Backend connection successful"

---

## 🎯 What You Should See

**Backend Window:**
```
Starting Wiki Quiz Backend Server...
Using SQLite database (wiki_quiz.db) - No PostgreSQL setup required!
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

**Frontend Window:**
```
Starting React development server...
Compiled successfully!
webpack compiled successfully
```

**Browser:**
- Wiki Quiz App interface
- Two tabs: "Generate Quiz" and "Past Quizzes"
- No error messages

---

## 🆘 Still Having Problems?

1. **Check both windows are open** (backend and frontend)
2. **Check `.env` file exists** in `backend/` folder
3. **Check API key is correct** in `.env` file
4. **Restart both servers** (close windows, run scripts again)
5. **Check browser console** (F12) for specific errors

---

**Follow these steps exactly, and everything should work!** ✅
