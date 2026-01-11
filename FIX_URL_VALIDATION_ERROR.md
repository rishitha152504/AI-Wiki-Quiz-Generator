# Fix: "URL must be a valid English Wikipedia article URL" Error

## Problem
The URL validation is too strict and rejecting valid URLs.

## Solution ✅

I've updated the scraper to:
- Remove whitespace from URLs
- Fix common URL format issues (http vs https, missing https://, etc.)
- Provide better error messages

## What to Do Now

### Step 1: Restart Backend Server

1. **In the backend window**, press **Ctrl+C** to stop the server
2. **Wait for it to stop**
3. **Start it again:**
   ```powershell
   python run.py
   ```

### Step 2: Try Again with Correct URL Format

**Make sure your URL is exactly:**
```
https://en.wikipedia.org/wiki/Alan_Turing
```

**Common mistakes to avoid:**
- ❌ `http://en.wikipedia.org/wiki/Alan_Turing` (missing 's' in https)
- ❌ `en.wikipedia.org/wiki/Alan_Turing` (missing https://)
- ❌ `https://en.wikipedia.org/wiki/Alan Turing` (space instead of underscore)
- ✅ `https://en.wikipedia.org/wiki/Alan_Turing` (correct!)

---

## Correct URL Format

**Template:**
```
https://en.wikipedia.org/wiki/Article_Name
```

**Examples:**
- ✅ `https://en.wikipedia.org/wiki/Alan_Turing`
- ✅ `https://en.wikipedia.org/wiki/Python_(programming_language)`
- ✅ `https://en.wikipedia.org/wiki/Artificial_intelligence`

**Note:** Use underscores `_` not spaces in article names!

---

## Quick Test URLs (Copy Exactly)

1. `https://en.wikipedia.org/wiki/Alan_Turing`
2. `https://en.wikipedia.org/wiki/Python_(programming_language)`
3. `https://en.wikipedia.org/wiki/Artificial_intelligence`
4. `https://en.wikipedia.org/wiki/Quantum_computing`
5. `https://en.wikipedia.org/wiki/Machine_learning`

---

## After Restarting Backend

1. **Restart backend** (Ctrl+C, then `python run.py`)
2. **Go to frontend:** http://localhost:3000
3. **Paste URL exactly:** `https://en.wikipedia.org/wiki/Alan_Turing`
4. **Click "Generate Quiz"**
5. **Should work now!** ✅

---

**Restart the backend and try again with the correct URL format!** 🚀
