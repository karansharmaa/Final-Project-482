import os
from src.score_movie import get_movie_sentiment  # Import the function from score_movie.py

def create_movie_list():
    """
    Creates a dictionary of movie names and sequential IDs.
    """
    movie_dict = {}
    movies_folder = "dataset/2_reviews_per_movie_raw/"
    movie_files = os.listdir(movies_folder)
    movie_names = [file.split('.')[0] for file in movie_files if file.endswith('.csv')]

    for i, movie in enumerate(movie_names):
        movie_dict[i] = movie  # Assign a sequential ID as the key

    return movie_dict

def get_movie_sentiment_analysis(movie_id):
    """
    Get simplified sentiment analysis for a specific movie based on its ID.
    """
    movie_dict = create_movie_list()

    if movie_id in movie_dict:
        selected_movie = movie_dict[movie_id]
        sentiment = get_movie_sentiment(selected_movie)

        # Simplify sentiment response
        average_sentiment = sentiment["average_sentiment"]
        if average_sentiment["compound"] > 0.5:
            sentiment_summary = "Positive"
        elif average_sentiment["compound"] < -0.5:
            sentiment_summary = "Negative"
        else:
            sentiment_summary = "Neutral"

        return {
            "movie_name": sentiment["movie_name"],
            "sentiment_summary": sentiment_summary,
            "average_rating": sentiment["average_rating"]
        }
    else:
        raise ValueError("Invalid movie ID.")




