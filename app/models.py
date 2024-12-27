from sqlalchemy import Column, Integer, String, Text, DateTime
from .database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    source = Column(String, nullable=True)
    url = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    published_at = Column(DateTime, nullable=True)
