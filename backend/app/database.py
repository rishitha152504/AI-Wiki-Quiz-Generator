from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Database Configuration
# Set DATABASE_URL in .env to use PostgreSQL
# Format: postgresql://username:password@host:port/database_name
# Example: postgresql://postgres:password@localhost:5432/wiki_quiz_db
# If DATABASE_URL is not set, defaults to SQLite for development
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # Default to SQLite for development
    DATABASE_URL = "sqlite:///./wiki_quiz.db"
    print("⚠️  Using SQLite database (wiki_quiz.db) - For production, use PostgreSQL!")
    print("   Set DATABASE_URL in .env to use PostgreSQL")
else:
    # Parse and display database info (hide password)
    if '@' in DATABASE_URL:
        db_info = DATABASE_URL.split('@')[-1]
        print(f"✅ Using PostgreSQL database: {db_info}")
    else:
        print(f"✅ Using database from DATABASE_URL")

# SQLite requires check_same_thread=False for FastAPI
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
