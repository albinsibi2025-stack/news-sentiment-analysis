from news_api import get_news
from sentiment import analyze_sentiment
from database import insert_news

news = get_news()

if news:
    articles = news["articles"]

    print(f"Total Articles: {len(articles)}\n")

    for article in articles:
        title = article["title"]
        description = article.get("description")
        source = article["source"]["name"]
        published_at = article["publishedAt"]

        label, score = analyze_sentiment(title)

        print(f"Title: {title}")
        print(f"Sentiment: {label}")
        print(f"Score: {score:.2f}")
        print("-" * 60)

        # Save to PostgreSQL
        insert_news(
            title,
            description,
            source,
            published_at,
            label,
            score
        )