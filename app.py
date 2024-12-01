from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
from src.choose_movie import create_movie_list, get_movie_sentiment_analysis

app = Flask(__name__)

# path to the dataset. please make sure the user saves the path to the dataset. this is imperative. 
MOVIE_REVIEWS_PATH = "dataset/2_reviews_per_movie_raw"

@app.route('/')
def index():
    # renders the main index page. 
    return render_template('index.html')

@app.route('/get-movie-list', methods=['GET'])
def get_movie_list():
    #provides a list of the movies that are available from the selection. 
    #this is fetched from our dataset. fetches the .csv file. 
    #once fetched, goes into it and the sentiment analysis nlp begins. 
    try:
        movie_dict = create_movie_list()  # Generate the movie list using choose_movie.py
        return jsonify({"movies": movie_dict})  # Send movie list to the frontend
    #error handling 
    except Exception as e:
        return jsonify({"error": f"Failed to fetch movie list: {str(e)}"}), 500
    
#access the get-sentiment methods. 
@app.route('/get-sentiment', methods=['POST'])
def get_sentiment():
    #provides the sentiment analysis of the movie 
    data = request.json
    try:
        movie_id = int(data.get('movie_id'))  # makes sure that movie id is an integer
        sentiment = get_movie_sentiment_analysis(movie_id)  # here is where the sentiment is accessed. 
        return jsonify(sentiment)
    #error handling
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"Failed to fetch sentiment: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

