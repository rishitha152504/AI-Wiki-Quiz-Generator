# PostgreSQL Installation Guide - Step by Step

## 🎯 Recommended Version

**Install: PostgreSQL 16.x** (Latest stable version)

Or if 16.x is not available, **PostgreSQL 15.x** also works perfectly.

---

## Step 1: Download PostgreSQL

1. **Go to:** https://www.postgresql.org/download/windows/

2. **Click:** "Download the installer"

3. **Choose:** 
   - **Version:** PostgreSQL 16 (or 15 if 16 not available)
   - **Platform:** Windows x86-64
   - **Download:** The Windows installer (usually 200-300 MB)

---

## Step 2: Install PostgreSQL

### Installation Steps:

1. **Run the installer** (postgresql-16-x64.exe or similar)

2. **Welcome Screen:**
   - Click "Next"

3. **Installation Directory:**
   - Keep default: `C:\Program Files\PostgreSQL\16`
   - Click "Next"

4. **Select Components:**
   - ✅ PostgreSQL Server (required)
   - ✅ pgAdmin 4 (recommended - GUI tool)
   - ✅ Stack Builder (optional - not needed)
   - ✅ Command Line Tools (recommended)
   - Click "Next"

5. **Data Directory:**
   - Keep default: `C:\Program Files\PostgreSQL\16\data`
   - Click "Next"

6. **Password:**
   - **IMPORTANT:** Set a password for the `postgres` user
   - **Remember this password!** You'll need it later
   - Example: `mypassword123` (use something you'll remember)
   - Click "Next"

7. **Port:**
   - Keep default: `5432`
   - Click "Next"

8. **Advanced Options:**
   - Locale: Keep default (or select your locale)
   - Click "Next"

9. **Pre Installation Summary:**
   - Review and click "Next"

10. **Installation:**
    - Wait for installation (2-5 minutes)
    - Click "Next" when complete

11. **Completing the Setup:**
    - **Uncheck** "Launch Stack Builder" (not needed)
    - Click "Finish"

---

## Step 3: Verify Installation

### Method 1: Check Services

1. **Press Windows key + R**
2. **Type:** `services.msc`
3. **Press Enter**
4. **Look for:** "postgresql-x64-16" (or your version)
5. **Status should be:** "Running"

### Method 2: Check pgAdmin

1. **Open pgAdmin 4** from Start menu
2. **Enter password** you set during installation
3. **You should see** PostgreSQL server in the left panel

---

## Step 4: Create Database

### Method 1: Using pgAdmin (Easiest) ⭐

1. **Open pgAdmin 4** from Start menu
2. **Enter your password** (the one you set during installation)
3. **Expand servers:**
   - Click "Servers" → "PostgreSQL 16"
4. **Right-click "Databases"**
5. **Select:** "Create" → "Database..."
6. **Database name:** `wiki_quiz_db`
7. **Click "Save"**

✅ Database created!

### Method 2: Using Command Line (psql)

1. **Open Command Prompt or PowerShell**

2. **Navigate to PostgreSQL bin folder:**
   ```powershell
   cd "C:\Program Files\PostgreSQL\16\bin"
   ```

3. **Connect to PostgreSQL:**
   ```powershell
   .\psql.exe -U postgres
   ```
   - Enter your password when prompted

4. **Create database:**
   ```sql
   CREATE DATABASE wiki_quiz_db;
   ```

5. **Verify:**
   ```sql
   \l
   ```
   - You should see `wiki_quiz_db` in the list

6. **Exit:**
   ```sql
   \q
   ```

---

## Step 5: Update .env File

1. **Go to:** `backend` folder

2. **Open:** `.env` file in Notepad (or any text editor)

3. **Add/Update DATABASE_URL:**
   ```env
   DATABASE_URL=postgresql://postgres:your_password@localhost:5432/wiki_quiz_db
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Replace `your_password`** with the password you set during PostgreSQL installation

   **Example:**
   ```env
   DATABASE_URL=postgresql://postgres:mypassword123@localhost:5432/wiki_quiz_db
   GEMINI_API_KEY=AIzaSyAbc123xyz789...
   ```

5. **Save the file**

---

## Step 6: Install PostgreSQL Driver

1. **Open PowerShell**

2. **Navigate to backend:**
   ```powershell
   cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\backend"
   ```

3. **Activate virtual environment:**
   ```powershell
   .\venv\Scripts\activate
   ```

4. **Install psycopg2-binary:**
   ```powershell
   pip install psycopg2-binary
   ```

   Wait for installation to complete.

---

## Step 7: Test the Connection

1. **Start backend:**
   ```powershell
   python run.py
   ```

2. **You should see:**
   ```
   ✅ Using PostgreSQL database: localhost:5432/wiki_quiz_db
   INFO:     Uvicorn running on http://0.0.0.0:8000
   ```

3. **If you see errors:**
   - Check PostgreSQL is running (services.msc)
   - Verify password in .env is correct
   - Check database name is correct

---

## Connection String Format

```
postgresql://username:password@host:port/database_name
```

**Your format:**
```
postgresql://postgres:your_password@localhost:5432/wiki_quiz_db
```

**Components:**
- `postgres` - Username (default PostgreSQL user)
- `your_password` - Password you set during installation
- `localhost` - Host (or 127.0.0.1)
- `5432` - Port (default PostgreSQL port)
- `wiki_quiz_db` - Database name

---

## Quick Checklist

- [ ] PostgreSQL 16.x (or 15.x) downloaded
- [ ] PostgreSQL installed with password set
- [ ] Database `wiki_quiz_db` created
- [ ] `.env` file updated with DATABASE_URL
- [ ] psycopg2-binary installed
- [ ] Backend starts without errors
- [ ] See "✅ Using PostgreSQL database" message

---

## Troubleshooting

### Problem: "Password authentication failed"

**Solution:**
- Check password in .env file matches the one you set during installation
- Make sure there are no extra spaces
- Try resetting PostgreSQL password if needed

### Problem: "Could not connect to server"

**Solution:**
- Make sure PostgreSQL service is running
- Check Windows Services (services.msc)
- Start PostgreSQL service if it's stopped

### Problem: "Database does not exist"

**Solution:**
- Create the database (see Step 4)
- Check database name in .env matches

### Problem: "ModuleNotFoundError: No module named 'psycopg2'"

**Solution:**
- Install psycopg2-binary: `pip install psycopg2-binary`
- Make sure virtual environment is activated

---

## Summary

✅ **Version:** PostgreSQL 16.x (or 15.x)
✅ **Password:** Remember the one you set!
✅ **Database:** `wiki_quiz_db`
✅ **Port:** 5432 (default)
✅ **Connection String:** `postgresql://postgres:password@localhost:5432/wiki_quiz_db`

**Follow these steps and you'll have PostgreSQL running!** 🚀
