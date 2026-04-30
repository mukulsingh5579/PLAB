#Dynamic "Price Drop" Web Watcher
import requests
from bs4 import BeautifulSoup
import time

URL = "https://example-store.com/product"
THRESHOLD = 500.00

def check_price():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Finding a hypothetical price tag
    price = float(soup.find(id="priceblock_ourprice").get_text().replace('$', ''))
    
    if price < THRESHOLD:
        print(f"Deal Alert! New Price: ${price}")
        return True
    return False

# Runs every hour
# while not check_price(): time.sleep(3600)