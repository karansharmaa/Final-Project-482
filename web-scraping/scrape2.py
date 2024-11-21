import requests
from bs4 import BeautifulSoup

# URL of the IMDb reviews page
url = "https://www.imdb.com/title/tt1375666/reviews"

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send a GET request to the URL with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all review containers
    reviews = soup.find_all('div', class_='review-container')

    # Extract and print the text of each review
    for review in reviews:
        # Get the review text
        review_text = review.find('div', class_='text show-more__control').get_text(strip=True)
        print(review_text)
        print("-----")  # Separator for clarity
else:
    print(f"Failed to retrieve reviews. Status code: {response.status_code}")