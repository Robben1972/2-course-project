import requests
from config import NEWS_API_KEY

BASE_URL = "https://newsapi.org/v2"

class NewsAPIService:
    def fetch_top_headlines(self, country="us"):
        url = f"{BASE_URL}/top-headlines?country={country}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def search_articles(self, keyword):
        url = f"{BASE_URL}/everything?q={keyword}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def fetch_by_category(self, category):
        url = f"{BASE_URL}/top-headlines?category={category}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
