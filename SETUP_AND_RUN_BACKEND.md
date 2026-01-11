# 🚀 Setup and Run Backend - Complete Guide

## Step 1: Verify Python Installation

1. **Open PowerShell** (new window)
2. **Type:** `python --version`
3. **You should see:** `Python 3.12.x` (or similar)

If you see a version number, Python is installed! ✅

---

## Step 2: Set Up Backend (Choose One Method)

### Method A: Use Setup Script (Easiest) ⭐

1. **Go to your QUIZ folder:**
   `C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ`

2. **Double-click:** `setup-backend-with-py.bat`

3. **Wait for it to complete** (may take 3-5 minutes)
   - Creates virtual environment
   - Installs all dependencies
   - Starts the server automatically

4. **You should see:**
   ```
   INFO:     Uvicorn running on http://0.0.0.0:8000
   INFO:     Application startup complete.
   ```

5. **Keep this window open!** (Don't close it)

---

### Method B: Manual Setup (If Script Doesn't Work)

**Open PowerShell and run these commands one by one:**

```powershell
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
```

```powershell
python -m venv venv
```

```powershell
.\venv\Scripts\activate
```

You should see `(venv)` at the start of your prompt.

```powershell
pip install --upgrade pip
```

```powershell
pip install -r requirements.txt
```

This may take a few minutes...

```powershell
python run.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Keep this window open!**

---

## Step 3: Verify Backend is Running

1. **Open a new browser tab**
2. **Go to:** http://localhost:8000/api/health
3. **You should see:**
   ```json
   {"status":"healthy","message":"Backend is running and ready","database":"connected"}
   ```

If you see this, backend is working! ✅

---

## Step 4: Connect Frontend to Backend

### Make Sure Frontend is Running

1. **Check if frontend is still running**
   - You should have a window with `npm start` running
   - If not, double-click `start-frontend.bat`

2. **Frontend should be at:** http://localhost:3000

### Test Connection

1. **Go to frontend:** http://localhost:3000
2. **Press F12** (open Developer Tools)
3. **Click "Console" tab**
4. **Look for:** `✅ Backend connection successful`

If you see this, frontend and backend are connected! ✅

---

## Step 5: Test the Full Application

1. **In the frontend** (http://localhost:3000)
2. **Make sure you're on "Generate Quiz" tab**
3. **URL should be filled:** `https://en.wikipedia.org/wiki/Alan_Turing`
4. **Click "Generate Quiz" button**
5. **Wait about 30 seconds** (it needs to scrape Wikipedia and generate quiz)
6. **Quiz should appear!** 🎉

---

## ✅ Success Checklist

- [ ] Python is installed (`python --version` works)
- [ ] Backend window is open and shows "Uvicorn running"
- [ ] http://localhost:8000/api/health shows healthy status
- [ ] Frontend is running at http://localhost:3000
- [ ] Frontend console shows "✅ Backend connection successful"
- [ ] Can generate a quiz successfully

---

## 🔧 Troubleshooting

### Backend won't start?

**Error: "GEMINI_API_KEY not set"**
- Check: `backend/.env` file exists
- We already created this, so it should be fine

**Error: "Port 8000 already in use"**
- Close other programs using port 8000
- Or restart computer

**Error: "Module not found"**
- Make sure virtual environment is activated
- Run: `pip install -r requirements.txt` again

### Frontend can't connect?

**Check:**
1. Backend window is still open and running
2. Test: http://localhost:8000/api/health works in browser
3. Check browser console (F12) for specific errors

**If still not connecting:**
- Restart backend (close window, run `setup-backend-with-py.bat` again)
- Restart frontend (close window, run `start-frontend.bat` again)
- Refresh browser (F5)

---

## 📋 Quick Commands Reference

**Start Backend:**
```powershell
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
.\venv\Scripts\activate
python run.py
```

**Start Frontend:**
```powershell
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\frontend"
npm start
```

**Test Backend:**
- Open: http://localhost:8000/api/health

**Test Frontend:**
- Open: http://localhost:3000

---

**Ready? Start with Step 2 (Method A - the easiest)!** 🚀
