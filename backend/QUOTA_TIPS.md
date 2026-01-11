# Quick Tips: Avoiding API Quota Errors

## ✅ Do This

1. **Use Cached Quizzes**
   - The app automatically caches all generated quizzes
   - If you see a quiz in "Past Quizzes", it won't use API quota
   - Click "Details" to view cached quizzes

2. **Wait Between Requests**
   - Free tier: 60 requests per minute
   - Wait at least 2 seconds between requests
   - Don't spam the "Generate Quiz" button

3. **Check History First**
   - Always check "Past Quizzes" tab before generating
   - Reuse existing quizzes when possible

## ❌ Avoid This

1. **Rapid Requests**
   - Don't generate 10+ quizzes in quick succession
   - Space out your requests

2. **Regenerating Same URLs**
   - The app caches quizzes, but if you delete and regenerate
   - You'll use quota again

3. **Very Long Articles**
   - Extremely long Wikipedia articles use more tokens
   - Try articles with moderate length

## 🔄 If You Hit the Limit

1. **Wait 1-2 minutes** - Rate limits reset every minute
2. **Check your usage** at https://aistudio.google.com/app/apikey
3. **Use cached quizzes** from the history tab
4. **Come back later** if you hit daily limits

## 📊 Free Tier Summary

- **60 requests/minute** - Very generous for normal use
- **1,500 requests/day** - Plenty for development
- **1M tokens/minute** - Usually not an issue

Most users won't hit these limits unless generating many quizzes rapidly!
