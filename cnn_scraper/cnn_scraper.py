from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from datetime import datetime
import csv

# Set the path to chromedriver
chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'

boundary_date = datetime(2022, 1, 1)

file = open('cnn_headlines.csv', 'w')
writer = csv.writer(file)

chrome_options = Options()

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

bad_dates = 0

def get_headlines(url):
    global bad_dates
    driver.get(url)
    time.sleep(3)

    full_page_source = driver.page_source

    soup = BeautifulSoup(full_page_source, 'html.parser')
    headlines = soup.find_all('span', class_="container__headline-text")
    dates = soup.find_all('div', class_='container__date')
    for headline, date in zip(headlines, dates):
        headline_text = headline.text.strip()
        date_text = date.text.strip()

        article_date = datetime.strptime(date_text, '%b %d, %Y')
        if article_date < boundary_date:
            bad_dates += 1
        else:
            writer.writerow([headline_text, date_text])
            print(headline_text)
            print(date_text)
            bad_dates = 0
        
        if bad_dates > 20:
            return False

    return True



base_url = 'https://edition.cnn.com/search?q=apple&from={}&size=10&page={}&sort=newest&types=all&section='

page_number = 1
while True:
    url = base_url.format((page_number-1)*10, page_number)
    print(f"Scraping headlines from page {page_number}...")
    if not get_headlines(url):
        break
    page_number += 1

driver.quit()
file.close()

