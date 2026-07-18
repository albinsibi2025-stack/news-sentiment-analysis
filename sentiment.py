from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of a text.

    Args:
        text (str): News title or description.

    Returns:
        tuple: (sentiment_label, sentiment_score)
    """

    if not text:
        return "Neutral", 0.0

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        label = "Positive"
    elif polarity < 0:
        label = "Negative"
    else:
        label = "Neutral"

    return label, polarity