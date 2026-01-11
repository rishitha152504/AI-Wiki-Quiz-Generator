# Complete Setup Guide - PostgreSQL + Frontend-Backend Connection

## Overview

This guide covers:
1. ✅ Switching from SQLite to PostgreSQL
2. ✅ Connecting frontend to backend (already configured!)

---

## Part 1: PostgreSQL Setup

### Quick Setup Steps

1. **Install PostgreSQL**
   - Download: https://www.postgresql.org/download/windows/
   - Install and remember your password

2. **Create Database**
   ```sql
   CREATE DATABASE wiki_quiz_db;
   ```

3. **Update .env File**
   ```env
   DATABASE_URL=postgresql://postgres:your_password@localhost:5432/wiki_quiz_db
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Install PostgreSQL Driver**
   ```powershell
   cd backend
   .\venv\Scripts\activate
   pip install psycopg2-binary
   ```

5. **Start Backend**
   ```powershell
   python run.py
   ```

**For detailed instructions, see: `POSTGRESQL_SETUP.md`**

---

## Part 2: Frontend-Backend Connection

### ✅ Already Configured!

Your frontend and backend are already properly connected:

- ✅ **CORS configured** in backend
- ✅ **API URL configured** in frontend
- ✅ **Health check endpoint** available
- ✅ **All endpoints** properly set up

### How to Test

1. **Start Backend:**
   ```powershell
   cd backend
   .\venv\Scripts\activate
   python run.py
   ```

2. **Start Frontend:**
   ```powershell
   cd frontend
   npm start
   ```

3. **Test Connection:**
   - Open: http://localhost:3000
   - Press F12 → Console tab
   - Should see: `✅ Backend connection successful`

**For detailed information, see: `CONNECT_FRONTEND_BACKEND.md`**

---

## Quick Start Commands

### Backend (PostgreSQL)

```powershell
# Navigate to backend
cd backend

# Activate virtual environment
.\venv\Scripts\activate

# Install PostgreSQL driver (if not installed)
pip install psycopg2-binary

# Start server
python run.py
```

### Frontend

```powershell
# Navigate to frontend
cd frontend

# Start development server
npm start
```

---

## Configuration Files

### Backend .env

**Location:** `backend/.env`

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/wiki_quiz_db
GEMINI_API_KEY=your_api_key_here
```

### Frontend .env (Optional)

**Location:** `frontend/.env`

```env
REACT_APP_API_URL=http://localhost:8000
```

(Default is already `http://localhost:8000`, so this is optional)

---

## Verification Checklist

### PostgreSQL Setup
- [ ] PostgreSQL installed
- [ ] Database `wiki_quiz_db` created
- [ ] `.env` file has DATABASE_URL
- [ ] psycopg2-binary installed
- [ ] Backend starts without errors

### Frontend-Backend Connection
- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] http://localhost:8000/api/health works
- [ ] Browser console shows connection success
- [ ] Can generate quizzes

---

## Troubleshooting

### PostgreSQL Issues

**See:** `POSTGRESQL_SETUP.md` - Troubleshooting section

### Connection Issues

**See:** `CONNECT_FRONTEND_BACKEND.md` - Troubleshooting section

---

## Files Created

1. **POSTGRESQL_SETUP.md** - Complete PostgreSQL setup guide
2. **CONNECT_FRONTEND_BACKEND.md** - Frontend-backend connection guide
3. **setup-postgresql.bat** - Helper script for PostgreSQL setup
4. **COMPLETE_SETUP_GUIDE.md** - This file

---

## Summary

✅ **PostgreSQL:** Follow `POSTGRESQL_SETUP.md`
✅ **Connection:** Already configured! See `CONNECT_FRONTEND_BACKEND.md`

**Everything is ready! Follow the guides and you'll be up and running!** 🚀
