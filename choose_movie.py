import os
from score_movie import get_movie_sentiment  # Import the function from score_movie.py

# Creates a dictionary of movie names and sequential IDs
def create_movie_list():
    movie_dict = {}
    movies_folder = "Dataset/2_reviews_per_movie_raw/"
    movie_files = os.listdir(movies_folder)
    movie_names = [file.split('.')[0] for file in movie_files if file.endswith('.csv')]

    for i, movie in enumerate(movie_names):
        movie_dict[i] = movie  # Assign a sequential ID as the key

    return movie_dict

def choose_movie():
    print("Choose a movie from the list below:")
    movie_dict = create_movie_list()

    # Display the movies with their sequential IDs
    for movie_id, movie_name in movie_dict.items():
        print(f"{movie_id}: {movie_name}")

    try:
        # Get user input and validate
        movie_id = int(input("\nEnter the movie ID: "))
        if movie_id in movie_dict:
            selected_movie = movie_dict[movie_id]
            
            # Call the get_movie_sentiment function from score_movie.py
            sentiment = get_movie_sentiment(selected_movie)
            
            # Display the sentiment analysis results
            print(f"\nMovie Name: {sentiment['movie_name']}")
            print("Average Sentiment:")
            print(f"  Negative Sentiment: {sentiment['average_sentiment']['negative']}")
            print(f"  Neutral Sentiment: {sentiment['average_sentiment']['neutral']}")
            print(f"  Positive Sentiment: {sentiment['average_sentiment']['positive']}")
            print(f"  Compound Sentiment: {sentiment['average_sentiment']['compound']}")
            print("\nAverage Rating:", sentiment['average_rating'])

        else:
            print("Invalid movie ID. Please try again.")
    except ValueError:
        print("Please enter a valid numeric movie ID.")

# Run the movie selection and sentiment analysis
choose_movie()

