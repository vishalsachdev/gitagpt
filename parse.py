import requests
import os 
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.uni.illinois.edu/" # replace with the URL you want to scrape

def save_page(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    filename = os.path.basename(link)
    # filename = link.split("/")[-1]
    with open(filename, "w") as f:
        f.write(str(soup))

def crawl_website(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    for link in soup.find_all("a"):
        if link.get("href"):
            link = urljoin(url, link.get("href"))
            if link.startswith(url):
                save_page(link)

crawl_website(url) 