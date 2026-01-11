from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict
from datetime import datetime


class QuizQuestion(BaseModel):
    question: str
    options: List[str]  # 4 options
    answer: str
    difficulty: str  # easy, medium, hard
    explanation: str


class KeyEntities(BaseModel):
    people: List[str] = []
    organizations: List[str] = []
    locations: List[str] = []


class WikiArticleResponse(BaseModel):
    id: int
    url: str
    title: str
    summary: str
    key_entities: KeyEntities
    sections: List[str]
    quiz: List[QuizQuestion]
    related_topics: List[str]
    created_at: datetime

    class Config:
        from_attributes = True


class WikiArticleCreate(BaseModel):
    url: str


class WikiArticleList(BaseModel):
    id: int
    url: str
    title: str
    created_at: datetime

    class Config:
        from_attributes = True
