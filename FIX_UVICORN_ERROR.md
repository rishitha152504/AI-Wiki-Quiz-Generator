# Fix: ModuleNotFoundError: No module named 'uvicorn'

## Problem
The `uvicorn` module (and other dependencies) are not installed in your virtual environment.

## Solution: Install Dependencies

### Step 1: Make Sure Virtual Environment is Activated

You should see `(venv)` at the start of your prompt. If not, run:
```powershell
.\venv\Scripts\activate
```

### Step 2: Install Dependencies

**Type this command:**
```powershell
pip install -r requirements.txt
```

**Press Enter** and wait (this may take 3-5 minutes)

You'll see packages being installed. Wait until you see the prompt again.

### Step 3: Start Server Again

After installation completes, run:
```powershell
python run.py
```

---

## Quick Fix (Copy & Paste)

```powershell
# Make sure venv is activated (you should see (venv))
.\venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt

# Start server
python run.py
```

---

## What Should Happen

After `pip install -r requirements.txt`, you should see:
```
Successfully installed fastapi-0.104.1 uvicorn-0.24.0 ...
```

Then when you run `python run.py`, you should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

**Install the dependencies first, then start the server!** 🚀
