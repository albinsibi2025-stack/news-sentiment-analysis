# 📰 News Sentiment Analysis

A Python-based data engineering and data science project that fetches the latest news articles using NewsAPI, analyzes their sentiment using Natural Language Processing (NLP), stores the results in PostgreSQL, and visualizes the data through a Streamlit dashboard. The application is containerized with Docker and is designed for deployment on AWS.

---

## 📌 Project Overview

This project automates the process of collecting news articles, determining whether each article has a positive, negative, or neutral sentiment, storing the processed data in a PostgreSQL database, and displaying the results through an interactive web dashboard.

---

## 🚀 Features

- Fetches the latest news using NewsAPI
- Performs sentiment analysis using TextBlob
- Stores processed data in PostgreSQL
- Displays news and sentiment in a Streamlit dashboard
- Dockerized for consistent deployment
- Ready for deployment to AWS (ECR & ECS)

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Requests | Fetch news from NewsAPI |
| TextBlob | Sentiment analysis |
| PostgreSQL | Database |
| Psycopg2 | PostgreSQL connection |
| Streamlit | Dashboard |
| Docker | Containerization |
| Git & GitHub | Version control |

---

## 📂 Project Structure

```
news_sentiment/
│
├── app.py
├── dashboard.py
├── database.py
├── news_api.py
├── sentiment.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/albinsibi2025-stack/news-sentiment-analysis.git
cd news-sentiment-analysis
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure NewsAPI

Create a `.env` file and add:

```env
NEWS_API_KEY=YOUR_NEWSAPI_KEY
```

---

## 🗄️ PostgreSQL Setup

Create a database named:

```
newsdb
```

Create the table:

```sql
CREATE TABLE news (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    source VARCHAR(100),
    published_at TIMESTAMP,
    sentiment_label VARCHAR(20),
    sentiment_score FLOAT
);
```

---

## ▶️ Run the Project

Fetch news and save to the database:

```bash
python app.py
```

Start the dashboard:

```bash
streamlit run dashboard.py
```

Open:

```
http://localhost:8501
```

---

## 🐳 Docker

Build the Docker image:

```bash
docker build -t news-sentiment-analysis .
```

Run the container:

```bash
docker run -p 8501:8501 news-sentiment-analysis
```

---

## 📊 Project Workflow

```
NewsAPI
   │
   ▼
Fetch News Articles
   │
   ▼
Sentiment Analysis (TextBlob)
   │
   ▼
Store Results in PostgreSQL
   │
   ▼
Streamlit Dashboard
   │
   ▼
User
```

---

## 📸 Dashboard

The Streamlit dashboard displays:

- Total news articles
- Positive sentiment count
- Negative sentiment count
- Neutral sentiment count
- News article table
- Interactive charts

---

## ☁️ Future Enhancements

- Deploy PostgreSQL using Amazon RDS
- Deploy application using Amazon ECS (Fargate)
- Store raw news data in Amazon S3
- Schedule news fetching using AWS Lambda and EventBridge
- Add filtering by source, date, and sentiment
- Implement user authentication

---

## 👨‍💻 Author

**Albin Sibi**

GitHub: https://github.com/albinsibi2025-stack

---

## 📄 License

This project is created for learning and internship purposes.