import requests
from bs4 import BeautifulSoup
import time
from utils import save_to_csv

def get_soup(url, headers=None):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    print(f"Failed: {url}")
    return None

def extract_data(soup):
    data = []
    items = soup.select('.item')  # Customize
    for item in items:
        title = item.select_one('.title')
        price = item.select_one('.price')
        data.append({
            'title': title.text.strip() if title else None,
            'price': price.text.strip() if price else None
        })
    return data

def paginate(base_url, pages=3):
    all_data = []
    for page in range(1, pages + 1):
        url = f"{base_url}?page={page}"
        print(f"Scraping {url}")
        soup = get_soup(url)
        if soup:
            all_data += extract_data(soup)
        time.sleep(1)
    return all_data

if __name__ == "__main__":
    base_url = "https://example.com/listings"
    data = paginate(base_url, pages=5)
    save_to_csv(data, 'static_data.csv')
