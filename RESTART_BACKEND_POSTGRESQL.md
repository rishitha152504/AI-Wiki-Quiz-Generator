# Restart Backend Server and Connect to PostgreSQL

## Step-by-Step Instructions

### Step 1: Stop Current Backend (If Running)

1. **Find the backend window** (where `python run.py` is running)
2. **Press Ctrl+C** to stop the server
3. **Wait until you see the prompt again**

If backend is not running, skip to Step 2.

---

### Step 2: Install PostgreSQL Driver (If Not Installed)

1. **Open PowerShell**
2. **Navigate to backend folder:**
   ```powershell
   cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
   ```

3. **Activate virtual environment:**
   ```powershell
   .\venv\Scripts\activate
   ```
   You should see `(venv)` at the start of your prompt.

4. **Install PostgreSQL driver:**
   ```powershell
   pip install psycopg2-binary
   ```

   Wait for installation to complete.

---

### Step 3: Verify .env File

1. **Check that .env file has:**
   ```env
   DATABASE_URL=postgresql://postgres:1234@localhost:5432/wiki_quiz_db
   GEMINI_API_KEY=your_api_key_here
   ```

   ✅ I can see you've already updated it with password `1234` - that's correct!

---

### Step 4: Make Sure PostgreSQL is Running

1. **Press Windows key + R**
2. **Type:** `services.msc`
3. **Press Enter**
4. **Look for:** "postgresql-x64-16" (or your version)
5. **Status should be:** "Running"

If it's not running, right-click → "Start"

---

### Step 5: Start Backend Server

1. **Make sure you're in backend folder:**
   ```powershell
   cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
   ```

2. **Activate virtual environment:**
   ```powershell
   .\venv\Scripts\activate
   ```

3. **Start the server:**
   ```powershell
   python run.py
   ```

---

### Step 6: Verify Connection

**You should see:**
```
✅ Using PostgreSQL database: localhost:5432/wiki_quiz_db
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

✅ **If you see "✅ Using PostgreSQL database", it's connected!**

---

### Step 7: Test the Connection

1. **Open browser**
2. **Go to:** http://localhost:8000/api/health
3. **You should see:**
   ```json
   {"status":"healthy","message":"Backend is running and ready","database":"connected"}
   ```

✅ **If you see this, PostgreSQL is connected and working!**

---

## Quick Command Summary

```powershell
# 1. Navigate to backend
cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"

# 2. Activate virtual environment
.\venv\Scripts\activate

# 3. Install PostgreSQL driver (if not installed)
pip install psycopg2-binary

# 4. Start server
python run.py
```

---

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'psycopg2'"

**Solution:**
```powershell
pip install psycopg2-binary
```

### Error: "password authentication failed"

**Solution:**
- Check password in .env file (should be `1234` - which you already have)
- Make sure PostgreSQL password is actually `1234`
- Verify no extra spaces in .env file

### Error: "could not connect to server"

**Solution:**
- Make sure PostgreSQL service is running (services.msc)
- Check PostgreSQL is installed correctly
- Verify port 5432 is not blocked

### Error: "database does not exist"

**Solution:**
- Create database: `wiki_quiz_db`
- Use pgAdmin or psql to create it
- See POSTGRESQL_INSTALL_GUIDE.md for instructions

### Server doesn't show "✅ Using PostgreSQL database"

**Solution:**
- Check .env file has DATABASE_URL set correctly
- Make sure no spaces around = sign
- Verify database name is correct: `wiki_quiz_db`

---

## Success Indicators

✅ Backend shows: "✅ Using PostgreSQL database: localhost:5432/wiki_quiz_db"
✅ No errors when starting server
✅ Health check works: http://localhost:8000/api/health
✅ Database status shows "connected"

---

**Follow these steps and your backend will connect to PostgreSQL!** 🚀
