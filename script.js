document.getElementById('review-form').addEventListener('submit', async function (event) {
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
