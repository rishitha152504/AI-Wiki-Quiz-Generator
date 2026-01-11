# Generate Your First Quiz - Step by Step

## Why You Don't Have Quizzes Yet

You're seeing "No quizzes generated yet" because:
- The API quota was hit before any quiz completed
- Quizzes are only saved after successful generation
- Once you generate one successfully, it will be cached forever!

## ✅ How to Generate Your First Quiz

### Step 1: Wait for API Quota to Reset

**Option A: Wait 1-2 Minutes (Rate Limit Reset)**
- The rate limit (60 requests/minute) resets quickly
- Wait 1-2 minutes
- Try again

**Option B: Wait for Daily Reset (If Daily Quota Hit)**
- Free tier resets daily (usually midnight UTC)
- Check your usage: https://aistudio.google.com/app/apikey
- Try again tomorrow if needed

---

### Step 2: Make Sure Both Servers Are Running

**Backend:**
- Check backend window is open
- Should see: `INFO:     Uvicorn running on http://0.0.0.0:8000`
- If not running, start it: `python run.py`

**Frontend:**
- Check frontend window is open
- Should see: `Compiled successfully`
- If not running, start it: `npm start`

---

### Step 3: Generate Your First Quiz

1. **Go to frontend:** http://localhost:3000 (or 3001)
2. **Click "Generate Quiz" tab**
3. **Use this URL (copy exactly):**
   ```
   https://en.wikipedia.org/wiki/Alan_Turing
   ```
4. **Click "Generate Quiz" button**
5. **Wait 30-60 seconds** (it needs to scrape Wikipedia and call API)
6. **Quiz should appear!** 🎉

---

### Step 4: After First Quiz is Generated

Once you successfully generate your first quiz:
- ✅ It will be saved in the database
- ✅ It will appear in "Past Quizzes" tab
- ✅ You can view it anytime without using API
- ✅ You can generate more quizzes (within quota limits)

---

## 🎯 Best Strategy

1. **Wait 1-2 minutes** for rate limit to reset
2. **Generate ONE quiz** successfully
3. **That quiz will be cached forever**
4. **You can view it anytime** in "Past Quizzes" tab
5. **Generate more quizzes** as quota allows

---

## 📋 Quick Checklist

Before generating:
- [ ] Waited 1-2 minutes (for rate limit reset)
- [ ] Backend is running (check backend window)
- [ ] Frontend is running (check frontend window)
- [ ] Using correct URL format: `https://en.wikipedia.org/wiki/Article_Name`
- [ ] Ready to wait 30-60 seconds for generation

---

## 🔄 What Happens When You Generate

1. **Frontend sends request** to backend
2. **Backend checks cache** (no quiz found yet)
3. **Backend scrapes Wikipedia** (takes 5-10 seconds)
4. **Backend calls Gemini API** (takes 10-20 seconds)
5. **Backend saves quiz** to database
6. **Backend returns quiz** to frontend
7. **Frontend displays quiz** 🎉

**Total time: 30-60 seconds**

---

## ⚠️ If You Still Get Quota Error

1. **Wait longer** (5-10 minutes)
2. **Check API usage:** https://aistudio.google.com/app/apikey
3. **Try again tomorrow** if daily quota is hit
4. **Consider getting a new API key** from a different Google account

---

## ✅ After First Success

Once you generate your first quiz:
- It will appear in "Past Quizzes" tab
- You can view it anytime (no API needed)
- You can take the quiz in "Quiz Mode"
- You can generate more quizzes (within limits)

---

**Wait 1-2 minutes, then try generating your first quiz!** 🚀
