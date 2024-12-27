from fastapi import APIRouter, HTTPException, Depends
from app.api_service import NewsAPIService

router = APIRouter()

@router.get("/top-headlines/")
def get_top_headlines(api_service: NewsAPIService = Depends(NewsAPIService)):
    try:
        return api_service.fetch_top_headlines()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/")
def search_news(keyword: str, api_service: NewsAPIService = Depends(NewsAPIService)):
    try:
        return api_service.search_articles(keyword)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/category/")
def get_news_by_category(category: str, api_service: NewsAPIService = Depends(NewsAPIService)):
    try:
        return api_service.fetch_by_category(category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
