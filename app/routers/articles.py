from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Article
from datetime import datetime

router = APIRouter()

@router.get("/saved/")
def get_saved_articles(db: Session = Depends(get_db)):
    return db.query(Article).all()

@router.post("/save/")
def save_article(article_data: dict, db: Session = Depends(get_db)):
    article = Article(
        title=article_data["title"],
        source=article_data.get("source"),
        url=article_data["url"],
        description=article_data.get("description"),
        published_at=article_data.get("published_at", datetime.now()),
    )
    try:
        db.add(article)
        db.commit()
        db.refresh(article)
        return {"message": "Article saved successfully", "id": article.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Article could not be saved")

@router.delete("/delete/{article_id}/")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    db.delete(article)
    db.commit()
    return {"message": "Article deleted successfully"}
