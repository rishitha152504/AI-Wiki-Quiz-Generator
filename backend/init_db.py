"""
Database initialization script
Creates all tables defined in models.py
"""
from app.database import engine, Base
from app.models import WikiArticle

def init_database():
    """Create all database tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_database()
