from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from sqlalchemy.sql import func
from app.database import Base


class WikiArticle(Base):
    """Model to store Wikipedia article data and generated quiz"""
    __tablename__ = "wiki_articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    summary = Column(Text)
    raw_html = Column(Text)  # Store raw HTML for reference
    key_entities = Column(JSON)  # Store as JSON: {"people": [], "organizations": [], "locations": []}
    sections = Column(JSON)  # Store as JSON array
    quiz = Column(JSON)  # Store quiz questions as JSON array
    related_topics = Column(JSON)  # Store as JSON array
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
