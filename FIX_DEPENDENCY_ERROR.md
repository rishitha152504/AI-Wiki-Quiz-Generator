# Fix: psycopg2-binary Installation Error

## Problem
The error occurs because `psycopg2-binary` (PostgreSQL adapter) requires PostgreSQL to be installed, but your project uses **SQLite by default** (which doesn't need PostgreSQL).

## Solution ✅

I've **removed `psycopg2-binary` from requirements.txt** because:
- ✅ Your project uses **SQLite by default** (no setup needed)
- ✅ PostgreSQL is **optional** (only if you set DATABASE_URL)
- ✅ SQLite works perfectly for this project

## What to Do Now

### Option 1: Run Setup Again (Recommended)

1. **Close the backend window** (if it's open)
2. **Double-click:** `setup-backend.bat` again
3. **It should work now!** ✅

### Option 2: Manual Install

If you want to continue manually:

```powershell
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
.\venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

---

## Why This Happened

- `psycopg2-binary` is for PostgreSQL databases
- Your project uses SQLite (which is included with Python)
- SQLite doesn't need any additional drivers
- The error happened because PostgreSQL isn't installed

## If You Need PostgreSQL Later

If you ever want to use PostgreSQL instead of SQLite:

1. Install PostgreSQL from: https://www.postgresql.org/download/
2. Uncomment the line in `requirements.txt`:
   ```
   psycopg2-binary==2.9.9
   ```
3. Set `DATABASE_URL` in `.env` file

**But for now, SQLite works perfectly!** ✅

---

## Next Steps

1. **Run `setup-backend.bat` again**
2. **It should install successfully now**
3. **Backend will start on port 8000**
4. **Connect frontend and test!**

---

**The fix is done! Just run the setup script again.** 🚀
