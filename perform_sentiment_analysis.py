from nltk.sentiment.vader import SentimentIntensityAnalyzer

def perform_sentiment_analysis(file_path):
    sid = SentimentIntensityAnalyzer()

    with open(file_path, 'r') as file:
        news_article = file.read()

    # Perform sentiment analysis
    sentiment_scores = sid.polarity_scores(news_article)
    return sentiment_scores
