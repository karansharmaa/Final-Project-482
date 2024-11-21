from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Path to the portable Chrome executable
chrome_binary_path = './GoogleChromePortableBeta/App/Chrome-bin/chrome.exe'  # Updated path

# Set up Chrome options
options = Options()
options.binary_location = chrome_binary_path  # Specify the portable Chrome binary location
options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging port
options.add_argument("--headless")  # Run in headless mode (optional)

# Path to the matching ChromeDriver
chromedriver_path = './chromedriver.exe'  # Ensure chromedriver is in your project directory

# Set up the ChromeDriver service
service = Service(chromedriver_path)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service, options=options)

# URL of the IMDb reviews page
url = "https://www.imdb.com/title/tt1375666/reviews"

# Load the page
driver.get(url)

# Wait for the page to load completely
time.sleep(3)  # Adjust the sleep time based on your network speed or use explicit waits

# Try a different CSS selector to extract reviews within the content container
reviews = driver.find_elements(By.CSS_SELECTOR, 'div.ipc-page-content-container .sc-16ede01-2')  # Adjusted selector for reviews

# Create an array to store the reviews
review_texts = []

# Loop through the reviews and extract the text
for review in reviews:
    review_texts.append(review.text)

# Print the array of reviews
print(review_texts)

# Close the driver when done
driver.quit()
