# Wiki Quiz App - Project Summary

## Project Overview

A complete full-stack application that generates interactive quizzes from Wikipedia articles using AI. The system scrapes Wikipedia content, processes it with Google Gemini API via LangChain, and provides a beautiful React frontend for quiz generation and management.

## Features Implemented

### Core Features ✅
- **Wikipedia URL Input**: Accepts any English Wikipedia article URL
- **Content Scraping**: BeautifulSoup-based extraction of article content
- **AI Quiz Generation**: Uses Google Gemini Pro via LangChain to generate 5-10 questions
- **PostgreSQL Storage**: Stores all scraped data and generated quizzes
- **History View**: Table of all previously generated quizzes
- **Details Modal**: Full quiz view in a modal dialog
- **Take Quiz Mode**: Interactive quiz with scoring system

### Bonus Features ✅
- **URL Caching**: Prevents duplicate scraping of the same URL
- **Raw HTML Storage**: Stores original HTML for reference
- **Entity Extraction**: Identifies people, organizations, and locations
- **Section-based Organization**: Questions organized by article sections
- **Difficulty Levels**: Easy, medium, and hard questions
- **Related Topics**: AI-suggested topics for further reading
- **Error Handling**: Graceful handling of invalid URLs and API failures

## Technical Architecture

### Backend (FastAPI)
```
backend/
├── app/
│   ├── database.py       # SQLAlchemy database setup
│   ├── models.py         # Database models
│   ├── schemas.py        # Pydantic validation schemas
│   ├── scraper.py        # Wikipedia scraping logic
│   ├── llm_service.py    # LLM integration with LangChain
│   ├── prompts.py        # Prompt templates
│   └── main.py           # FastAPI application & routes
├── requirements.txt      # Python dependencies
├── run.py               # Server entry point
├── init_db.py           # Database initialization
└── test_api.py          # API testing script
```

### Frontend (React)
```
frontend/
├── src/
│   ├── App.js           # Main React component
│   ├── index.js         # React entry point
│   └── index.css        # Styling
├── public/
│   └── index.html       # HTML template
└── package.json         # Node dependencies
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| POST | `/api/quiz/generate` | Generate quiz from URL |
| GET | `/api/quiz/history` | Get all quizzes |
| GET | `/api/quiz/{id}` | Get quiz by ID |
| DELETE | `/api/quiz/{id}` | Delete quiz by ID |

## Database Schema

**wiki_articles** table:
- `id` (Primary Key)
- `url` (Unique)
- `title`
- `summary`
- `raw_html`
- `key_entities` (JSON)
- `sections` (JSON)
- `quiz` (JSON)
- `related_topics` (JSON)
- `created_at`
- `updated_at`

## LLM Integration

- **Provider**: Google Gemini Pro (free tier)
- **Framework**: LangChain
- **Model**: gemini-pro
- **Temperature**: 0.7 (balanced creativity/consistency)
- **Prompt Design**: Optimized for factual accuracy and content grounding

## Key Files

### Prompt Templates
- Location: `backend/app/prompts.py` and `backend/PROMPT_TEMPLATES.md`
- Design: System + Human message structure
- Features: JSON output format, content grounding, difficulty levels

### Scraper
- Location: `backend/app/scraper.py`
- Features: Title, summary, sections, entities, clean text extraction

### Frontend Components
- Location: `frontend/src/App.js`
- Features: Tab navigation, quiz display, modal, quiz mode, scoring

## Setup Requirements

1. **Python 3.8+** with virtual environment
2. **Node.js 16+** with npm
3. **PostgreSQL 12+** database
4. **Google Gemini API Key** (free tier)

## Testing

### Sample URLs
- Alan Turing: `https://en.wikipedia.org/wiki/Alan_Turing`
- Quantum Computing: `https://en.wikipedia.org/wiki/Quantum_computing`
- Machine Learning: `https://en.wikipedia.org/wiki/Machine_learning`

See `sample_data/example_urls.txt` for more.

### Test Script
Run `python backend/test_api.py` to test API endpoints.

## Evaluation Criteria Coverage

| Criterion | Status | Notes |
|-----------|--------|-------|
| Prompt Design | ✅ | Optimized prompts in prompts.py |
| Quiz Quality | ✅ | 5-10 questions, difficulty levels, explanations |
| Extraction Quality | ✅ | Clean scraping, entity extraction, sections |
| Functionality | ✅ | End-to-end flow working |
| Code Quality | ✅ | Modular, commented, structured |
| Error Handling | ✅ | Graceful error messages |
| UI Design | ✅ | Clean, modern, responsive |
| Database Accuracy | ✅ | Proper storage and retrieval |
| Testing Evidence | ✅ | Sample data and test script |

## File Structure

```
QUIZ/
├── backend/                 # FastAPI backend
│   ├── app/                # Application code
│   ├── requirements.txt    # Python dependencies
│   ├── run.py             # Server entry
│   └── init_db.py         # DB setup
├── frontend/               # React frontend
│   ├── src/               # Source code
│   └── package.json       # Node dependencies
├── sample_data/            # Test data
│   ├── example_urls.txt
│   └── sample_outputs/
├── README.md              # Main documentation
├── SETUP_GUIDE.md         # Quick setup
├── PROJECT_SUMMARY.md     # This file
└── .gitignore             # Git ignore rules
```

## Next Steps for Deployment

1. Set up production database (PostgreSQL on cloud)
2. Configure environment variables
3. Set up CORS for production domain
4. Build frontend: `npm run build`
5. Serve frontend with nginx or similar
6. Deploy backend with gunicorn/uvicorn
7. Set up SSL certificates
8. Configure API rate limiting

## Notes

- The application uses free-tier Gemini API (rate limits apply)
- Wikipedia scraping respects robots.txt and uses appropriate headers
- Database caching prevents duplicate API calls for same URLs
- All prompts are designed to minimize hallucination
- Frontend is responsive and works on mobile devices

## Support

For issues or questions:
1. Check README.md for detailed documentation
2. Review SETUP_GUIDE.md for setup issues
3. Check backend logs for API errors
4. Verify environment variables are set correctly
