# 🐍 Install Python - Complete Guide

## Problem
Python is not found on your system. You need to install Python to run the backend.

## Solution: Install Python

### Step 1: Download Python

1. **Go to:** https://www.python.org/downloads/
2. **Click:** "Download Python 3.12.x" (or latest version)
3. **Wait for download to complete**

### Step 2: Install Python

1. **Run the installer** (python-3.12.x-amd64.exe)
2. **IMPORTANT:** Check this box: ✅ **"Add Python to PATH"**
   - This is at the bottom of the first installation screen
   - **This is critical!** Without it, Python won't work in PowerShell
3. **Click:** "Install Now"
4. **Wait for installation** (2-3 minutes)
5. **Click:** "Close" when done

### Step 3: Verify Installation

1. **Close ALL PowerShell/Command Prompt windows**
2. **Open a NEW PowerShell window**
3. **Type:** `python --version`
4. **You should see:** `Python 3.12.x` (or similar)

If you see a version number, Python is installed! ✅

### Step 4: Restart Your Computer

**Important:** After installing Python, restart your computer to ensure everything is set up correctly.

---

## After Installing Python

### Step 1: Run the Fix Script

1. **Double-click:** `fix-backend-python.bat`
2. **Wait for it to complete**
3. **Then run:** `start-backend.bat`

### Step 2: Or Manual Setup

Open PowerShell and run:

```powershell
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

---

## Alternative: Use Python Launcher (py)

If `python` doesn't work, try `py` instead:

```powershell
py --version
```

If this works, use `py` instead of `python` in all commands:

```powershell
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
py run.py
```

---

## Quick Checklist

- [ ] Python downloaded from python.org
- [ ] ✅ "Add Python to PATH" was checked during installation
- [ ] Computer restarted after installation
- [ ] `python --version` shows a version number
- [ ] Virtual environment created successfully
- [ ] Backend server starts without errors

---

## Still Having Issues?

### Issue: "Python was not found" after installation

**Fix:**
1. Uninstall Python
2. Reinstall Python
3. **Make sure to check "Add Python to PATH"**
4. Restart computer
5. Try again

### Issue: Python works in some terminals but not others

**Fix:**
- Close ALL terminal windows
- Restart computer
- Open NEW PowerShell window
- Try again

### Issue: "pip is not recognized"

**Fix:**
- Make sure Python was installed with "pip" (it's included by default)
- Try: `python -m pip --version`
- If that works, use `python -m pip` instead of just `pip`

---

**Install Python first, then we can set up the backend!** 🚀
