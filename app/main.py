from fastapi import FastAPI
from app.routers import news, articles
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="News Aggregator")

# Register routers
app.include_router(news.router, prefix="/news", tags=["News"])
app.include_router(articles.router, prefix="/articles", tags=["Articles"])
