#Minimalist Web Scraper
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Get the first 5 news titles
titles = soup.find_all("span", class_="titleline")[:5]
for i, title in enumerate(titles, 1):
    print(f"{i}. {title.get_text()}")