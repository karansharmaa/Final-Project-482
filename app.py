from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
from src.choose_movie import create_movie_list, get_movie_sentiment_analysis

app = Flask(__name__)

# Paths to dataset folders
MOVIE_REVIEWS_PATH = "dataset/2_reviews_per_movie_raw"

@app.route('/')
def index():
    """
    Render the main index page.
    """
    return render_template('index.html')

@app.route('/get-movie-list', methods=['GET'])
def get_movie_list():
    """
    Provide a list of movies available for selection.
    """
    try:
        movie_dict = create_movie_list()  # Generate the movie list using choose_movie.py
        return jsonify({"movies": movie_dict})  # Send movie list to the frontend
    except Exception as e:
        return jsonify({"error": f"Failed to fetch movie list: {str(e)}"}), 500

@app.route('/get-sentiment', methods=['POST'])
def get_sentiment():
    """
    Provide sentiment analysis for a selected movie.
    """
    data = request.json
    try:
        movie_id = int(data.get('movie_id'))  # Ensure movie_id is an integer
        sentiment = get_movie_sentiment_analysis(movie_id)  # Get sentiment for the movie
        return jsonify(sentiment)
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"Failed to fetch sentiment: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

