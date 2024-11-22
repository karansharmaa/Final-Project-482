import pandas as pd

# Function to process reviews and metadata
def process_movie_data(movie_name, movie_year):
    # Path to the reviews CSV file (e.g., "The Dark Knight 2008.csv")
    review_file = f"Dataset/2_reviews_per_movie_raw/{movie_name} {movie_year}.csv"
    
    try:
        # Read the reviews CSV for the movie
        reviews_df = pd.read_csv(review_file)
        
        # Check if required columns exist and filter out missing values
        if all(col in reviews_df.columns for col in ['rating', 'date', 'title', 'review']):
            # Filter out rows with missing review data
            reviews_df = reviews_df.dropna(subset=['rating', 'review'])
            
            # Get an array of the first 3 reviews
            reviews = reviews_df.head(3)[['rating', 'date', 'title', 'review']].to_dict('records')
            
            return reviews
        else:
            return None
    
    except FileNotFoundError:
        return None

# Function to extract movie metadata and reviews
def get_movie_info(movie_data):
    # Store results in a list of dictionaries
    result = []
    
    for _, row in movie_data.head(2).iterrows():  # Limiting to first 2 movies for demo
        movie_name = row['name']
        movie_year = int(row['year'])
        rating = row['rating']
        genres = row['genres']
        release_date = row['release_date']
        
        # Collect metadata
        movie_metadata = {
            'name': movie_name,
            'year': movie_year,
            'rating': rating,
            'genres': genres,
            'release_date': release_date
        }
        
        # Get reviews for the movie
        reviews = process_movie_data(movie_name, movie_year)
        
        # Append metadata and reviews to the result list
        result.append({
            'movie_metadata': movie_metadata,
            'reviews': reviews if reviews else 'No reviews found'
        })
    
    return result

# Example: Load movie data for a specific genre
movie_data = pd.read_csv("Dataset/1_movies_per_genre/Action.csv")  # Example for Action genre

# Get the movie info for the first 2 movies (or adjust number for more)
movie_info = get_movie_info(movie_data)

# Print the output for each movie
for movie in movie_info:
    print(f"Movie Name: {movie['movie_metadata']['name']} ({movie['movie_metadata']['year']})")
    print(f"Rating: {movie['movie_metadata']['rating']}, Genres: {movie['movie_metadata']['genres']}")
    print(f"Release Date: {movie['movie_metadata']['release_date']}")
    print("Reviews:")
    if isinstance(movie['reviews'], list):
        for review in movie['reviews']:
            # Print only the first 200 characters of the review
            snippet = review['review'][:200] + '...' if len(review['review']) > 200 else review['review']
            print(f"  - Rating: {review['rating']}, Date: {review['date']}")
            print(f"    Title: {review['title']}")
            print(f"    Review: {snippet}\n")
    else:
        print(f"  - {movie['reviews']}\n")





