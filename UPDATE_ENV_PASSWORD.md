# Update .env File - Replace Password

## ✅ DATABASE_URL Added!

I've added the DATABASE_URL line to your `.env` file. Now you need to replace the password.

---

## Step 1: Open .env File

1. **Go to:** `backend` folder
2. **Open:** `.env` file in Notepad

---

## Step 2: Replace YOUR_PASSWORD

**Current line:**
```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/wiki_quiz_db
```

**Replace `YOUR_PASSWORD` with your actual PostgreSQL password**

**Example:**
If your PostgreSQL password is `mypassword123`, change it to:
```env
DATABASE_URL=postgresql://postgres:mypassword123@localhost:5432/wiki_quiz_db
```

---

## Step 3: Save the File

1. **Save** the file (Ctrl+S)
2. **Close** Notepad

---

## Important Notes

- ✅ **Use the password you set during PostgreSQL installation**
- ✅ **No spaces** around the = sign
- ✅ **No spaces** in the password (if your password has spaces, keep them)
- ✅ **Keep the quotes** if your password has special characters

---

## Final .env File Should Look Like:

```env
# Database Configuration
# For SQLite (default - no setup required):
# Leave DATABASE_URL empty or unset to use SQLite

# For PostgreSQL (production):
DATABASE_URL=postgresql://postgres:YOUR_ACTUAL_PASSWORD@localhost:5432/wiki_quiz_db

# Gemini API Key (Required)
GEMINI_API_KEY=AIzaSyDcWowH-rUwWfLf-Jhui7r3mee3I6BtP4E
```

---

## After Updating Password

1. **Save the .env file**
2. **Restart backend server** (if running)
3. **Test connection:** `python run.py`
4. **Should see:** `✅ Using PostgreSQL database: localhost:5432/wiki_quiz_db`

---

**Open backend/.env and replace YOUR_PASSWORD with your actual PostgreSQL password!** 🔑
