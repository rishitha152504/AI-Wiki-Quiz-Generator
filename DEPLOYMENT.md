# Deployment Guide

This guide explains how to deploy the Wiki Quiz App to production.

## Frontend Deployment (Vercel)

### 1. Deploy Frontend to Vercel

1. Push your code to GitHub
2. Go to [Vercel](https://vercel.com) and import your repository
3. Configure the build settings:
   - **Framework Preset**: Create React App
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`

### 2. Set Environment Variables in Vercel

In your Vercel project settings, add the following environment variable:

```
REACT_APP_API_URL=https://your-backend-url.com
```

Replace `https://your-backend-url.com` with your actual backend deployment URL.

## Backend Deployment

### Option 1: Railway (Recommended)

1. Go to [Railway](https://railway.app)
2. Create a new project and connect your GitHub repository
3. Add a new service and select your repository
4. Set the **Root Directory** to `backend`
5. Configure the start command: `python run.py` or `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add environment variables:
   - `GROQ_API_KEY`: Your Groq API key
   - `DATABASE_URL`: PostgreSQL connection string (Railway provides this automatically if you add a PostgreSQL service)
   - `ALLOWED_ORIGINS`: Your Vercel frontend URL (e.g., `https://your-app.vercel.app`)
   - `ENVIRONMENT`: `production`

### Option 2: Render

1. Go to [Render](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables (same as Railway)

### Option 3: Heroku

1. Install Heroku CLI
2. Create a `Procfile` in the `backend` directory:
   ```
   web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
3. Deploy using Heroku CLI or GitHub integration
4. Set environment variables in Heroku dashboard

## Environment Variables

### Backend (.env)

```env
GROQ_API_KEY=your_groq_api_key_here
DATABASE_URL=postgresql://user:password@host:port/database
ALLOWED_ORIGINS=https://your-frontend.vercel.app
ENVIRONMENT=production
```

### Frontend (Vercel Environment Variables)

```
REACT_APP_API_URL=https://your-backend.railway.app
```

## Important Notes

1. **CORS Configuration**: The backend is configured to allow all origins in production. For better security, set `ALLOWED_ORIGINS` to your specific frontend URL.

2. **Database**: Make sure to set up a PostgreSQL database in your backend hosting platform (Railway, Render, etc.)

3. **API Key**: Get your free Groq API key from [console.groq.com](https://console.groq.com/keys)

4. **Health Check**: The backend has a health check endpoint at `/api/health` that the frontend uses to verify connectivity.

## Testing the Deployment

1. After deploying both frontend and backend, test the connection:
   - Visit your Vercel frontend URL
   - Try generating a quiz
   - Check browser console for any CORS or connection errors

2. If you see connection errors:
   - Verify `REACT_APP_API_URL` is set correctly in Vercel
   - Check that the backend is running and accessible
   - Verify CORS settings in the backend allow your frontend domain
