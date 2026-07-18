import streamlit as st
import pandas as pd
import psycopg2

# Database connection
conn = psycopg2.connect(
    host="host.docker.internal",
    port="5432",
    database="newsdb",
    user="postgres",
    password="root"
)

# Read data
query = "SELECT * FROM news;"
df = pd.read_sql(query, conn)

st.title("📰 News Sentiment Analysis Dashboard")

st.subheader("News Data")
st.dataframe(df)

# Metrics
st.subheader("Statistics")

st.write("Total Articles:", len(df))
st.write("Positive:", len(df[df["sentiment_label"] == "Positive"]))
st.write("Negative:", len(df[df["sentiment_label"] == "Negative"]))
st.write("Neutral:", len(df[df["sentiment_label"] == "Neutral"]))

# Bar chart
st.subheader("Sentiment Distribution")

sentiment_counts = df["sentiment_label"].value_counts()

st.bar_chart(sentiment_counts)