/*document.getElementById('review-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const mediaType = document.getElementById('mediaType').value;
    const mediaName = document.getElementById('mediaName').value;

    try {
        const response = await fetch('http://localhost:5000/api/review', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ mediaType, mediaName })
        });

        if (!response.ok) throw new Error('Failed to fetch review');

        const data = await response.json();
        document.getElementById('rating').textContent = data.rating || 'N/A';
        document.getElementById('summary').textContent = data.summary || 'N/A';
    } catch (error) {
        console.error('Error:', error);
        alert('Error fetching review');
    }
});
*/
// Here is where we fetch and populate the movie list. 
async function fetchMovies() 
{
    try 
    {
        const response = await fetch('/get-movie-list');
        const data = await response.json();

        const movieSelect = document.getElementById('movieSelect');

        for (const [id, movie] of Object.entries(data.movies))
        {
            const option = document.createElement('option');
            option.value = id;
            option.textContent = movie;
            movieSelect.appendChild(option);
        }
    } catch (error) 
    {
        console.error('Could not fetch movies. Error:', error);
        alert('Unable to load movies. Refresh or re-run.');
    }
}

// Fetch sentiment analysis for the selected movie
document.getElementById('movie-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const movieId = document.getElementById('movieSelect').value;

    try
    {
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

        // Once a movie has been and user demands results, the dialog is populated with simplified results from the sentiment analysis performed. 
        document.getElementById('movieName').textContent = `Movie: ${data.movie_name}`;
        document.getElementById('averageSentiment').textContent = `Overall Vibe: ${data.sentiment_summary}`;
        document.getElementById('averageRating').textContent = `Average IMDB Rating: ${data.average_rating}`;
    } catch (error) 
    {
        console.error('Unable to fetch sentiment:', error);
        alert('Failed to fetch sentiment. Refresh or re-run.');
    }
});

fetchMovies();
