



import requests
from bs4 import BeautifulSoup
from scrapingbee import ScrapingBeeClient

api_key = 'TD3NGAM3CAY0K7A9ASCN0TK3EJ4QHJ26JBL7U0VIH0WSPPZ49PERVRY67BSQ3DGSOKS5EWRXIZL8DDZP'
scraper = ScrapingBeeClient(api_key)

# Website to scrape
url = 'https://www.uni.illinois.edu/'

# Make the request
response = scraper.get(url)

# Get the HTML content
html_content = response.text

# Use BeautifulSoup to extract all the links
soup = BeautifulSoup(html_content, 'html.parser')
links = soup.find_all('a')

# Iterate over all the links
for link in links:
    link_url = link.get('href')
    # Make sure the link is not None and it's not a mailto link
    if link_url and not link_url.startswith('mailto:'):
        # Make the request
        response = scraper.get(link_url)
        # Get the HTML content
        html_content = response.text
        # Save the HTML content to a file
        with open(link_url.replace('/', '_')+'.html', 'w') as file:
            file.write(html_content)