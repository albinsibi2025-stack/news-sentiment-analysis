import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

URL = "https://newsapi.org/v2/top-headlines"

def get_news(country="us"):
    params = {
        "country": country,
        "apiKey": API_KEY
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        print(response.text)
        return None