import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon if it's not already downloaded
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to process reviews and metadata
def process_movie_data(movie_name):
    review_file = f"Dataset/2_reviews_per_movie_raw/{movie_name}.csv"
    
    try:
        # Read the reviews CSV for the movie
        reviews_df = pd.read_csv(review_file)
        
        # Check if required columns exist and filter out missing values
        if all(col in reviews_df.columns for col in ['rating', 'review']):
            # Filter out rows with missing review data
            reviews_df = reviews_df.dropna(subset=['rating', 'review'])
            
            return reviews_df
        else:
            return None
    
    except FileNotFoundError:
        return None

# Function to calculate average sentiment of reviews
def calculate_average_sentiment(reviews_df):
    # Initialize totals
    total_neg, total_neu, total_pos, total_compound = 0, 0, 0, 0
    
    # Loop through each review and calculate sentiment scores
    for review in reviews_df['review']:
        sentiment_scores = sia.polarity_scores(review)
        total_neg += sentiment_scores['neg']
        total_neu += sentiment_scores['neu']
        total_pos += sentiment_scores['pos']
        total_compound += sentiment_scores['compound']
    
    # Calculate averages
    num_reviews = len(reviews_df)
    avg_neg = total_neg / num_reviews
    avg_neu = total_neu / num_reviews
    avg_pos = total_pos / num_reviews
    avg_compound = total_compound / num_reviews
    
    return avg_neg, avg_neu, avg_pos, avg_compound

# Function to calculate average rating
def calculate_average_rating(reviews_df):
    # Convert ratings to numeric for averaging
    reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
    return reviews_df['rating'].mean()

# Function to get movie sentiment and metadata
def get_movie_sentiment(movie_name):
    reviews_df = process_movie_data(movie_name)
    
    if reviews_df is not None and not reviews_df.empty:
        # Calculate sentiment
        avg_neg, avg_neu, avg_pos, avg_compound = calculate_average_sentiment(reviews_df)
        
        # Calculate average rating
        avg_rating = calculate_average_rating(reviews_df)
    else:
        avg_neg = avg_neu = avg_pos = avg_compound = 'No reviews found'
        avg_rating = 'N/A'
    
    return {
        'movie_name': movie_name,
        'average_sentiment': {
            'negative': avg_neg,
            'neutral': avg_neu,
            'positive': avg_pos,
            'compound': avg_compound
        },
        'average_rating': avg_rating
    }
























