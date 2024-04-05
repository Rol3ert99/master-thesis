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

boundary_date = datetime(2023, 1, 1)

file = open('cnbc_headlines.csv', 'w')
writer = csv.writer(file)

chrome_options = Options()

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.cnbc.com/search/?query=APPLE&qsearchterm=APPLE'
driver.get(url)
time.sleep(5)

accept_cookies_button = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
accept_cookies_button.click()
time.sleep(5)

sort_by_newest_button = driver.find_element(By.XPATH, '//*[@id="sortdate"]')
sort_by_newest_button.click()
time.sleep(5)

printed_headlines = set()

scroll_pause_time = 2
screen_height = driver.execute_script("return window.screen.height;")
i = 1
while True:
    driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
    i += 1
    time.sleep(scroll_pause_time)

    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if screen_height * i > scroll_height:
        break

    full_page_source = driver.page_source
    soup = BeautifulSoup(full_page_source, 'html.parser')
    headlines = soup.find_all('span', class_="Card-title")
    dates = soup.find_all('span', class_='SearchResult-publishedDate')
    for headline, date in zip(headlines, dates):
        headline_text = headline.text.strip()
        date_text = date.text.strip()
        space_position = date_text.find(' ')
        date_text = date_text[:space_position]

        article_date = datetime.strptime(date_text, '%m/%d/%Y')
        if article_date < boundary_date:
            break

        if headline_text not in printed_headlines:
            printed_headlines.add(headline_text)
            writer.writerow([headline_text, date_text])
            print(headline_text)
            print(date_text)
    

driver.quit()
file.close()



# //*[@id="onetrust-accept-btn-handler"] - button accept cookies xpath

# //*[@id="sortdate"] - sort by newest button xpath

# <span class="SearchResult-publishedDate">3/18/2024 8:07:32 AM</span> - date element

