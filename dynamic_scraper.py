from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from utils import save_to_csv

def start_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    service = Service()
    return webdriver.Chrome(service=service, options=options)

def extract_data(driver):
    data = []
    items = driver.find_elements(By.CSS_SELECTOR, '.item')  # Customize
    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, '.title').text
            price = item.find_element(By.CSS_SELECTOR, '.price').text
        except:
            title, price = None, None
        data.append({'title': title, 'price': price})
    return data

def paginate(driver, base_url, pages=3):
    all_data = []
    for page in range(1, pages + 1):
        url = f"{base_url}?page={page}"
        driver.get(url)
        time.sleep(2)
        all_data += extract_data(driver)
    return all_data

if __name__ == "__main__":
    base_url = "https://example.com/listings"
    driver = start_driver(headless=False)
    data = paginate(driver, base_url, pages=5)
    save_to_csv(data, 'dynamic_data.csv')
    driver.quit()
