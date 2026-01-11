# Fix: Backend Not Starting

## Problem
When you run `start-backend.bat`, it shows "Press any key to continue" but nothing happens after that.

## Quick Solutions

### Solution 1: Run Diagnostic Tool First

1. **Double-click:** `test-backend-setup.bat`
2. This will check everything and tell you what's wrong
3. Fix any issues it finds
4. Then try `start-backend.bat` again

---

### Solution 2: Manual Start (Shows Real Errors)

1. **Open PowerShell**
   - Press Windows key
   - Type "PowerShell"
   - Press Enter

2. **Navigate to backend folder:**
   ```powershell
   cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
   ```

3. **Activate virtual environment:**
   ```powershell
   .\venv\Scripts\activate
   ```

4. **Start the server:**
   ```powershell
   python run.py
   ```

5. **This will show you the ACTUAL error** (if any)

---

## Common Issues & Fixes

### Issue 1: Python Not Installed

**Check:** Open PowerShell, type `python --version`

**If you see an error:**
- Download Python from: https://www.python.org/downloads/
- During installation, check "Add Python to PATH"
- Restart computer after installation
- Try again

### Issue 2: Virtual Environment Not Created

**Fix:** The script should create it automatically, but if it fails:

```powershell
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

### Issue 3: .env File Missing

**Fix:** We already created this, but verify it exists:

1. Go to: `backend` folder
2. Check if `.env` file exists
3. If not, create it with:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

### Issue 4: Port 8000 Already in Use

**Fix:**
- Close other programs using port 8000
- Or restart computer
- Or change port in `backend/run.py` (line 7) to 8001

### Issue 5: Dependencies Not Installed

**Fix:**
```powershell
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
.\venv\Scripts\activate
pip install -r requirements.txt
```

---

## Step-by-Step Manual Start

If scripts don't work, use these commands:

### Step 1: Open PowerShell
Press Windows key → Type "PowerShell" → Enter

### Step 2: Go to Backend Folder
```powershell
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
```

### Step 3: Activate Virtual Environment
```powershell
.\venv\Scripts\activate
```

You should see `(venv)` at the start of your prompt.

### Step 4: Install Dependencies (if needed)
```powershell
pip install -r requirements.txt
```

### Step 5: Start Server
```powershell
python run.py
```

### Step 6: You Should See:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

---

## What Should Happen

When backend starts successfully, you'll see:

```
Starting Wiki Quiz Backend Server...
Using SQLite database (wiki_quiz.db) - No PostgreSQL setup required!
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**Keep this window open!** The server is running.

---

## Verify Backend is Running

1. **Open browser**
2. **Go to:** http://localhost:8000/api/health
3. **Should see:**
   ```json
   {"status":"healthy","message":"Backend is running and ready","database":"connected"}
   ```

If you see this, backend is working! ✅

---

## Still Not Working?

1. **Run diagnostic:** `test-backend-setup.bat`
2. **Try manual start** (see Solution 2 above)
3. **Check the error message** - it will tell you exactly what's wrong
4. **Share the error** and I'll help you fix it

---

**Try the manual start method first - it will show you the actual error!**
