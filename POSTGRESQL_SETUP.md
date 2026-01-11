# PostgreSQL Setup Guide - Complete Instructions

## Overview

This guide will help you switch from SQLite to PostgreSQL for the Wiki Quiz App.

---

## Step 1: Install PostgreSQL

### Windows Installation

1. **Download PostgreSQL:**
   - Go to: https://www.postgresql.org/download/windows/
   - Click "Download the installer"
   - Download the latest version (e.g., PostgreSQL 16.x)

2. **Run the Installer:**
   - Double-click the downloaded file
   - Click "Next" through the wizard
   - **Important:** Remember the password you set for the `postgres` user!
   - Port: Keep default (5432)
   - Locale: Default is fine
   - Click "Next" until installation completes

3. **Verify Installation:**
   - PostgreSQL should start automatically
   - Look for "PostgreSQL" in your Windows services

---

## Step 2: Create Database

### Method 1: Using pgAdmin (GUI - Recommended)

1. **Open pgAdmin:**
   - Search for "pgAdmin" in Windows Start menu
   - Open pgAdmin 4

2. **Connect to Server:**
   - Enter the password you set during installation
   - Click "OK"

3. **Create Database:**
   - Right-click on "Databases"
   - Select "Create" → "Database"
   - Name: `wiki_quiz_db`
   - Click "Save"

### Method 2: Using Command Line (psql)

1. **Open Command Prompt or PowerShell**

2. **Connect to PostgreSQL:**
   ```powershell
   psql -U postgres
   ```
   - Enter your password when prompted

3. **Create Database:**
   ```sql
   CREATE DATABASE wiki_quiz_db;
   ```

4. **Exit psql:**
   ```sql
   \q
   ```

---

## Step 3: Update .env File

1. **Open:** `backend/.env`

2. **Add/Update DATABASE_URL:**
   ```env
   DATABASE_URL=postgresql://postgres:your_password@localhost:5432/wiki_quiz_db
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   **Replace:**
   - `postgres` - Your PostgreSQL username (usually `postgres`)
   - `your_password` - The password you set during PostgreSQL installation
   - `wiki_quiz_db` - Database name (you can change this if you want)

3. **Example:**
   ```env
   DATABASE_URL=postgresql://postgres:mypassword123@localhost:5432/wiki_quiz_db
   GEMINI_API_KEY=AIzaSyAbc123xyz789...
   ```

4. **Save the file**

---

## Step 4: Install PostgreSQL Driver

1. **Activate virtual environment:**
   ```powershell
   cd backend
   .\venv\Scripts\activate
   ```

2. **Install psycopg2-binary:**
   ```powershell
   pip install psycopg2-binary
   ```

   Or reinstall all requirements:
   ```powershell
   pip install -r requirements.txt
   ```

---

## Step 5: Initialize Database Tables

1. **Make sure backend is stopped** (Ctrl+C if running)

2. **Run initialization:**
   ```powershell
   python init_db.py
   ```

   Or the tables will be created automatically when you start the server.

---

## Step 6: Start Backend Server

1. **Start the backend:**
   ```powershell
   python run.py
   ```

2. **You should see:**
   ```
   Using database from DATABASE_URL: localhost:5432/wiki_quiz_db
   INFO:     Uvicorn running on http://0.0.0.0:8000
   ```

3. **If you see errors:**
   - Check PostgreSQL is running
   - Verify DATABASE_URL in .env is correct
   - Check username and password are correct
   - Make sure database exists

---

## Step 7: Verify Connection

1. **Test backend:**
   - Open: http://localhost:8000/api/health
   - Should see: `{"status":"healthy","database":"connected"}`

2. **Check backend logs:**
   - Should see database connection message
   - No connection errors

---

## Troubleshooting

### Error: "FATAL: password authentication failed"

**Solution:**
- Check your password in .env file
- Make sure there are no extra spaces
- Try resetting PostgreSQL password

### Error: "could not connect to server"

**Solution:**
- Make sure PostgreSQL is running
- Check Windows Services for "postgresql-x64-16" (or your version)
- Start the service if it's not running

### Error: "database does not exist"

**Solution:**
- Create the database (see Step 2)
- Check database name in .env matches

### Error: "ModuleNotFoundError: No module named 'psycopg2'"

**Solution:**
- Install psycopg2-binary: `pip install psycopg2-binary`
- Make sure virtual environment is activated

### Error: "relation does not exist"

**Solution:**
- Run: `python init_db.py`
- Or restart backend (tables create automatically)

---

## Connection String Format

```
postgresql://username:password@host:port/database_name
```

**Example:**
```
postgresql://postgres:mypassword@localhost:5432/wiki_quiz_db
```

**Components:**
- `postgres` - Username
- `mypassword` - Password
- `localhost` - Host (or 127.0.0.1)
- `5432` - Port (default PostgreSQL port)
- `wiki_quiz_db` - Database name

---

## Switching Back to SQLite (If Needed)

If you want to switch back to SQLite:

1. **Comment out or remove DATABASE_URL** from .env:
   ```env
   # DATABASE_URL=postgresql://postgres:password@localhost:5432/wiki_quiz_db
   GEMINI_API_KEY=your_key_here
   ```

2. **Restart backend**

3. **It will use SQLite automatically**

---

## Frontend-Backend Connection

The frontend is already configured to connect to the backend:

1. **Frontend uses:** `http://localhost:8000` (default)
2. **Backend runs on:** `http://localhost:8000`
3. **CORS is configured** to allow frontend connections

**No changes needed for frontend-backend connection!**

---

## Quick Checklist

- [ ] PostgreSQL installed
- [ ] Database `wiki_quiz_db` created
- [ ] `.env` file updated with DATABASE_URL
- [ ] psycopg2-binary installed
- [ ] Backend server starts without errors
- [ ] Health check works: http://localhost:8000/api/health
- [ ] Frontend connects successfully

---

**Follow these steps and you'll have PostgreSQL running!** 🚀
