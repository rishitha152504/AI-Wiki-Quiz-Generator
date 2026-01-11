# 🔧 Manual Backend Setup - Step by Step

## Complete Manual Guide to Start Backend

### Step 1: Open PowerShell

1. **Press Windows key**
2. **Type:** `PowerShell`
3. **Press Enter**
4. PowerShell window opens

---

### Step 2: Navigate to Backend Folder

**Copy and paste this command:**

```powershell
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
```

**Press Enter**

You should see the prompt change to show the backend folder path.

---

### Step 3: Check if Virtual Environment Exists

**Type this command:**

```powershell
Test-Path venv
```

**If it says `True`:** Virtual environment exists, go to Step 4
**If it says `False`:** Virtual environment doesn't exist, create it first (see below)

**To create virtual environment (if needed):**
```powershell
python -m venv venv
```
Wait for it to complete (may take 1-2 minutes)

---

### Step 4: Activate Virtual Environment

**Type this command:**

```powershell
.\venv\Scripts\activate
```

**Press Enter**

**You should see `(venv)` at the start of your prompt:**
```
(venv) PS C:\Users\dines\...\backend>
```

If you see `(venv)`, the virtual environment is activated! ✅

---

### Step 5: Verify Python is Working

**Type this command:**

```powershell
python --version
```

**You should see:** `Python 3.12.x` (or similar version)

If you see a version number, Python is working! ✅

---

### Step 6: Install/Update Dependencies

**Type this command:**

```powershell
pip install --upgrade pip
```

**Press Enter** and wait for it to complete.

**Then type:**

```powershell
pip install -r requirements.txt
```

**Press Enter** and wait (this may take 3-5 minutes)

You should see packages being installed. Wait until you see the prompt again.

---

### Step 7: Check .env File

**Type this command:**

```powershell
Test-Path .env
```

**If it says `True`:** .env file exists, go to Step 8
**If it says `False`:** You need to create it (see below)

**To check .env file content:**
```powershell
Get-Content .env
```

You should see:
```
GEMINI_API_KEY=your_api_key_here
```

If the file doesn't exist or doesn't have the API key, create it:
```powershell
notepad .env
```

Add this line:
```
GEMINI_API_KEY=your_actual_api_key_here
```

Save and close Notepad.

---

### Step 8: Start the Backend Server

**Type this command:**

```powershell
python run.py
```

**Press Enter**

**You should see:**
```
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Keep this window open!** The server is running. ✅

---

### Step 9: Test Backend is Working

1. **Open a new browser tab**
2. **Go to:** http://localhost:8000/api/health
3. **You should see:**
   ```json
   {"status":"healthy","message":"Backend is running and ready","database":"connected"}
   ```

If you see this, backend is working! ✅

---

## ✅ Success Checklist

- [ ] PowerShell opened
- [ ] Navigated to backend folder
- [ ] Virtual environment activated (see `(venv)` in prompt)
- [ ] Dependencies installed
- [ ] .env file exists with API key
- [ ] Server started (see "Uvicorn running")
- [ ] Health check works in browser

---

## 🔧 Troubleshooting

### Problem: "python is not recognized"

**Solution:**
- Python is not installed or not in PATH
- Install Python from: https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation
- Restart computer after installation

### Problem: "venv\Scripts\activate" not found

**Solution:**
- Virtual environment doesn't exist
- Create it: `python -m venv venv`
- Wait for it to complete
- Then activate: `.\venv\Scripts\activate`

### Problem: "Module not found" errors

**Solution:**
- Dependencies not installed
- Run: `pip install -r requirements.txt`
- Make sure virtual environment is activated (see `(venv)`)

### Problem: "GEMINI_API_KEY not set"

**Solution:**
- .env file doesn't exist or is empty
- Create .env file: `notepad .env`
- Add: `GEMINI_API_KEY=your_api_key_here`
- Save and restart server

### Problem: "Port 8000 already in use"

**Solution:**
- Another program is using port 8000
- Close other programs
- Or change port in `run.py` (line 7) to 8001

---

## 📋 Quick Command Reference

```powershell
# Navigate to backend
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start server
python run.py
```

---

## 🎯 After Backend is Running

1. **Keep the PowerShell window open** (don't close it)
2. **Test in browser:** http://localhost:8000/api/health
3. **Start frontend** (if not already running)
4. **Connect and test the full app**

---

**Follow these steps one by one, and your backend will be running!** 🚀
