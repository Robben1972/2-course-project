# **News Aggregator**

The **News Aggregator** application allows users to fetch news articles from a public API, save their favorite articles in a SQLite database, and manage these saved articles. It is built with **FastAPI** for the backend, **SQLAlchemy** for database management, and integrates with a public news API.

---

## **Features**
- Fetch news articles by keyword, category, or top headlines.
- Save articles locally to a SQLite database.
- View and manage saved articles.
- Graceful handling of API errors and notifications for no results.

---

## **Getting Started**
Follow these instructions to set up and run the project on your local machine.

### **Prerequisites**
- **Python 3.8+** installed on your system.
- An active internet connection to fetch news from the public API.

---

### **Installation**

1. **Clone the Repository**
   ```bash
   git clone [git@github.com:Robben1972/NewsAPIFastAPI.git](https://github.com/Robben1972/NewsAPIFastAPI.git)
   cd NewsAPIFastAPI
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required Python libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Get an API Key**
   - Register for an API key from a public news API like [NewsAPI](https://newsapi.org/).
   - Once you have the key, create a `config.py` file in the `app` directory:
     ```python
     NEWS_API_KEY = "your_api_key_here"
     ```

---

### **Running the Application**

1. **Run the Server**
   Start the FastAPI server using `uvicorn`:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API Documentation**
   - Open your browser and navigate to `http://127.0.0.1:8000/docs` for the Swagger UI.
   - Alternatively, use `http://127.0.0.1:8000/redoc` for ReDoc documentation.

---

### **API Endpoints**

#### **News Endpoints**
| Method | Endpoint            | Description                        |
|--------|---------------------|------------------------------------|
| GET    | `/news/top-headlines/` | Fetch top headlines.               |
| GET    | `/news/search/`        | Search news by keyword.            |
| GET    | `/news/category/`      | Fetch news by category.            |

#### **Articles Endpoints**
| Method | Endpoint               | Description                        |
|--------|------------------------|------------------------------------|
| GET    | `/articles/saved/`     | View all saved articles.           |
| POST   | `/articles/save/`      | Save an article to the database.   |
| DELETE | `/articles/delete/{id}/` | Delete a saved article by ID.      |

---

### **Project Structure**
```
NewsAPIFastAPI/
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI entry point
│   ├── api_service.py  # Handles API interactions
│   ├── models.py       # SQLAlchemy ORM models
│   ├── database.py     # Database connection and setup
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── news.py     # News fetching endpoints
│   │   ├── articles.py # Saved articles management
├── config.py           # Configuration (API key)
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---
