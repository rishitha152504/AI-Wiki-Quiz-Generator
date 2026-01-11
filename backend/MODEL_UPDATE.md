# Model Update: gemini-pro → gemini-2.0-flash-001

## Issue
The error `404 models/gemini-pro is not found` occurs because older model names are deprecated.

## Solution
Updated the model name to `gemini-2.0-flash-001` (stable version) in `backend/app/llm_service.py`.

## Available Models (2025)

### Current Models:
- **gemini-2.0-flash-001** ✅ (Currently used - stable, fast, free tier friendly)
- **gemini-2.5-flash** (Latest stable flash model)
- **gemini-2.5-pro** (Latest pro model, higher quality)
- **gemini-flash-latest** (Always uses latest flash)
- **gemini-pro-latest** (Always uses latest pro)

### Deprecated:
- ~~gemini-pro~~ ❌ (No longer available)
- ~~gemini-1.5-flash~~ ❌ (No longer available)
- ~~gemini-1.5-pro~~ ❌ (No longer available)

## To Switch Models

If you want to use `gemini-1.5-pro` instead (for higher quality):

1. Open `backend/app/llm_service.py`
2. Find line 17: `model="gemini-1.5-flash"`
3. Change to: `model="gemini-1.5-pro"`
4. Restart the backend server

## Notes

- Both models are available on the free tier
- `gemini-1.5-flash` is faster and more cost-effective
- `gemini-1.5-pro` provides higher quality responses
- The change is backward compatible - no other code changes needed
