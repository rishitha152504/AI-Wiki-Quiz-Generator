# AI-Wiki-Quiz-Generator

A full-stack application that generates quizzes from Wikipedia articles using Large Language Models (LLM). The system scrapes Wikipedia content, processes it with Google Gemini API via LangChain, and stores the generated quizzes in a PostgreSQL database.

## Features

- **Tab 1 - Generate Quiz**: Input a Wikipedia URL and automatically generate 5-10 quiz questions
- **Tab 2 - Past Quizzes**: View history of all previously generated quizzes
- **Take Quiz Mode**: Interactive quiz mode with scoring
- **Details Modal**: View full quiz details from history
- **Caching**: Prevents duplicate scraping of the same URL
- **Entity Extraction**: Identifies people, organizations, and locations
- **Section-based Questions**: Questions organized by article sections
- **Difficulty Levels**: Easy, medium, and hard questions

## Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **PostgreSQL**: Relational database
- **SQLAlchemy**: ORM for database operations
- **BeautifulSoup**: Web scraping
- **LangChain**: LLM framework
- **Google Gemini API**: Free-tier LLM for quiz generation

### Frontend
- **React**: UI framework
- **Axios**: HTTP client
- **CSS3**: Modern styling with gradients and animations

## Project Structure

```
QUIZ/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   │   ├── database.py      # Database configuration
│   │   │   ├── models.py        # SQLAlchemy models
│   │   │   ├── schemas.py       # Pydantic schemas
│   │   │   ├── scraper.py       # Wikipedia scraper
│   │   │   ├── llm_service.py   # LLM quiz generation
│   │   │   └── main.py          # FastAPI application
│   ├── requirements.txt
│   ├── run.py
│   └── .env.example
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── index.css
│   └── package.json
├── sample_data/
│   ├── example_urls.txt
│   └── sample_outputs/
└── README.md
```

## 🚀 Quick Start

**Windows Users:** Simply double-click `start-backend.bat` and `start-frontend.bat` (in separate terminals)

**For detailed setup and troubleshooting, see:**
- `QUICK_START.md` - Fast setup guide
- `CONNECTION_GUIDE.md` - Complete connection troubleshooting

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 16+
- SQLite (default, no setup required) OR PostgreSQL 12+ (optional)
- Google Gemini API Key (free tier available at https://makersuite.google.com/app/apikey)

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database:**
   ```bash
   # Create database
   createdb wiki_quiz_db
   ```

5. **Configure environment variables:**
   ```bash
   # Copy .env.example to .env
   cp .env.example .env
   # Edit .env and add your credentials
   DATABASE_URL=postgresql://username:password@localhost:5432/wiki_quiz_db
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

6. **Run the backend server:**
   ```bash
   python run.py
   # Or using uvicorn directly
   uvicorn app.main:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000`
   API documentation: `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

   The frontend will be available at `http://localhost:3000`

## API Endpoints

### POST `/api/quiz/generate`
Generate a quiz from a Wikipedia article URL.

**Request Body:**
```json
{
  "url": "https://en.wikipedia.org/wiki/Alan_Turing"
}
```

**Response:**
```json
{
  "id": 1,
  "url": "https://en.wikipedia.org/wiki/Alan_Turing",
  "title": "Alan Turing",
  "summary": "Alan Turing was a British mathematician...",
  "key_entities": {
    "people": ["Alan Turing"],
    "organizations": ["University of Cambridge"],
    "locations": ["United Kingdom"]
  },
  "sections": ["Early life", "World War II", "Legacy"],
  "quiz": [
    {
      "question": "Where did Alan Turing study?",
      "options": ["Harvard University", "Cambridge University", "Oxford University", "Princeton University"],
      "answer": "Cambridge University",
      "difficulty": "easy",
      "explanation": "Mentioned in the 'Early life' section."
    }
  ],
  "related_topics": ["Cryptography", "Enigma machine"]
}
```

### GET `/api/quiz/history`
Get list of all previously generated quizzes.

**Response:**
```json
[
  {
    "id": 1,
    "url": "https://en.wikipedia.org/wiki/Alan_Turing",
    "title": "Alan Turing",
    "created_at": "2024-01-15T10:30:00"
  }
]
```

### GET `/api/quiz/{article_id}`
Get detailed quiz information by article ID.

### DELETE `/api/quiz/{article_id}`
Delete a quiz by article ID.

## LangChain Prompt Templates

The quiz generation uses a carefully designed prompt template to ensure high-quality, factual questions. The prompt is located in `backend/app/llm_service.py`.

### Key Prompt Features:

1. **System Instructions**: Defines the role as an expert quiz generator
2. **Requirements**: Specifies question count, format, difficulty levels
3. **Output Format**: Enforces JSON structure for consistent parsing
4. **Content Grounding**: Emphasizes questions must be answerable from provided content
5. **Anti-Hallucination**: Explicitly avoids questions requiring external knowledge

### Prompt Template Structure:

```
System Message:
- Role definition
- Requirements (5-10 questions, 4 options, difficulty levels, explanations)
- Output format specification
- Content grounding instructions

Human Message:
- Article title
- Article sections
- Article content (truncated to 6000 chars for token limits)
```

The prompt is optimized to:
- Minimize hallucination by grounding questions in provided content
- Ensure diversity across article sections
- Generate appropriate difficulty levels
- Create plausible distractors
- Provide clear explanations

## Testing

### Sample Wikipedia URLs

Test the application with these URLs:

1. **Alan Turing**: `https://en.wikipedia.org/wiki/Alan_Turing`
2. **Quantum Computing**: `https://en.wikipedia.org/wiki/Quantum_computing`
3. **Machine Learning**: `https://en.wikipedia.org/wiki/Machine_learning`
4. **Photosynthesis**: `https://en.wikipedia.org/wiki/Photosynthesis`
5. **Renaissance**: `https://en.wikipedia.org/wiki/Renaissance`

See `sample_data/example_urls.txt` for more examples.

### Testing Steps

1. **Start backend server** (port 8000)
2. **Start frontend server** (port 3000)
3. **Open browser** to `http://localhost:3000`
4. **Generate Quiz Tab**:
   - Enter a Wikipedia URL
   - Click "Generate Quiz"
   - Wait for processing (scraping + LLM generation)
   - Review generated quiz
   - Try "Take Quiz Mode" for interactive testing
5. **Past Quizzes Tab**:
   - View all generated quizzes
   - Click "Details" to see full quiz in modal
   - Test quiz mode in modal as well

## Database Schema

### `wiki_articles` Table

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| url | String | Unique Wikipedia URL |
| title | String | Article title |
| summary | Text | First paragraph summary |
| raw_html | Text | Full HTML content (for reference) |
| key_entities | JSON | People, organizations, locations |
| sections | JSON | Array of section headings |
| quiz | JSON | Array of quiz questions |
| related_topics | JSON | Array of related topics |
| created_at | DateTime | Creation timestamp |
| updated_at | DateTime | Last update timestamp |

## Error Handling

The application handles:
- Invalid Wikipedia URLs
- Network errors during scraping
- LLM API failures
- Database connection errors
- Missing article sections
- JSON parsing errors

All errors are gracefully handled with user-friendly messages.

## Bonus Features Implemented

✅ **Take Quiz Mode**: Interactive quiz with scoring  
✅ **URL Validation**: Validates Wikipedia URLs before processing  
✅ **Caching**: Prevents duplicate scraping (checks database first)  
✅ **Raw HTML Storage**: Stores scraped HTML for reference  
✅ **Section-wise Grouping**: Questions organized by article sections  
✅ **Entity Extraction**: Identifies people, organizations, locations  

## Troubleshooting

### Backend Issues

1. **Database Connection Error**:
   - Verify PostgreSQL is running
   - Check DATABASE_URL in .env
   - Ensure database exists

2. **Gemini API Error**:
   - Verify GEMINI_API_KEY is set correctly
   - Check API quota/limits
   - Ensure internet connection

3. **Import Errors**:
   - Activate virtual environment
   - Reinstall requirements: `pip install -r requirements.txt`

### Frontend Issues

1. **API Connection Error**:
   - Verify backend is running on port 8000
   - Check CORS settings in backend
   - Verify API_BASE_URL in App.js

2. **Build Errors**:
   - Clear node_modules: `rm -rf node_modules && npm install`
   - Check Node.js version (16+ required)

## Future Enhancements

- User authentication and personal quiz collections
- Export quizzes to PDF/JSON
- Quiz sharing via unique links
- Advanced filtering and search in history
- Multiple LLM provider support
- Batch URL processing
- Quiz difficulty adjustment slider

## License

This project is open source and available for educational purposes.

## Author

AI-Wiki-Quiz-Generator - Built with FastAPI, React, and Google Gemini

