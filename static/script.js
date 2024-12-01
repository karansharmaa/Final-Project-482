// Here is where we fetch and populate the movie list. 
async function fetchMovies() 
{
    try 
    {
        //get the list of movies using json
        const response = await fetch('/get-movie-list');
        const data = await response.json();

        //populate the dropdown menu of movies 
        const movieSelect = document.getElementById('movieSelect');

        //drop down menu
        for (const [id, movie] of Object.entries(data.movies))
        {
            const option = document.createElement('option');
            option.value = id;
            option.textContent = movie;
            movieSelect.appendChild(option);
        }

    //error handling 
    } catch (error) 
    {
        console.error('Could not fetch movies. Error:', error);
        alert('Unable to load movies. Refresh or re-run.');
    }
}

// Fetch sentiment analysis for the movie selected by the user 
document.getElementById('movie-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const movieId = document.getElementById('movieSelect').value;

    //access the get-sentiment file, run that script and perform a sentiment analysis of the reviews
    //in the dataset. this comes in handy for generating the "overall vibe" section. 
    //aggregation 
    try
    {
        //also shows a log of what is happening in the backend console. 
        const response = await fetch('/get-sentiment', 
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ movie_id: movieId }),
        });

        const data = await response.json();

        if (data.error)
        {
            alert(data.error);
            return;
        }

        // once a movie has been and user demands results, the dialog is populated with simplified results from the sentiment analysis performed. 
        document.getElementById('movieName').textContent = `Movie: ${data.movie_name}`;
        document.getElementById('averageSentiment').textContent = `Overall Vibe: ${data.sentiment_summary}`;
        document.getElementById('averageRating').textContent = `Average IMDB Rating: ${data.average_rating}`;
        //error handling 
    } catch (error) 
    {
        console.error('Unable to fetch sentiment:', error);
        alert('Failed to fetch sentiment. Refresh or re-run.');
    }
});

fetchMovies();
