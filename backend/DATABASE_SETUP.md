# Database Setup Guide

## Quick Start (SQLite - Recommended for Development)

The application now uses **SQLite by default**, which requires **NO setup**! 

✅ **Already Done**: Database initialized successfully!

The database file `wiki_quiz.db` has been created in the `backend/` directory.

## Using SQLite (Current Setup)

- ✅ No installation required
- ✅ No server setup needed
- ✅ Works immediately
- ✅ Perfect for development

**No action needed** - you're all set!

## Using PostgreSQL (Optional - for Production)

If you want to use PostgreSQL instead:

### 1. Install PostgreSQL
- Download from: https://www.postgresql.org/download/windows/
- Install and remember your password

### 2. Create Database
```sql
CREATE DATABASE wiki_quiz_db;
```

### 3. Update .env file
Edit `backend/.env` and set:
```
DATABASE_URL=postgresql://username:password@localhost:5432/wiki_quiz_db
```

Replace:
- `username` with your PostgreSQL username (usually `postgres`)
- `password` with your PostgreSQL password

### 4. Restart the application
The app will automatically use PostgreSQL instead of SQLite.

## Current Status

✅ Database: SQLite (wiki_quiz.db)
✅ Tables created successfully
✅ Ready to use!

## Next Steps

1. Make sure you have your Gemini API key in `.env`
2. Start the backend: `python run.py`
3. Start the frontend: `npm start` (in frontend directory)
