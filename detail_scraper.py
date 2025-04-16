from selenium.webdriver.common.by import By
from utils import save_to_csv
import time

def get_detail_links(driver, listing_url):
    driver.get(listing_url)
    time.sleep(2)
    links = driver.find_elements(By.CSS_SELECTOR, '.item a')  # Adjust
    return [link.get_attribute('href') for link in links]

def scrape_detail(driver, url):
    driver.get(url)
    time.sleep(2)
    try:
        title = driver.find_element(By.CSS_SELECTOR, 'h1.title').text
        description = driver.find_element(By.CSS_SELECTOR, '.description').text
    except:
        title, description = None, None
    return {'url': url, 'title': title, 'description': description}

def scrape_all_details(driver, urls):
    return [scrape_detail(driver, url) for url in urls]

# Usage pattern:
# detail_urls = get_detail_links(driver, "https://example.com/listings")
# detail_data = scrape_all_details(driver, detail_urls)
