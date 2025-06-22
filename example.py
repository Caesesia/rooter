import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find and print the quotes
quotes = soup.find_all('span', class_='text')

for i, quote in enumerate(quotes, start=1):
    print(f"{i}. {quote.text}")

