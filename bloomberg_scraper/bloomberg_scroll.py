from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

# Set the path to the browser driver (ChromeDriver)
chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'

chrome_options = Options()

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.bloomberg.com/search?query=AAPL"
driver.get(url)
time.sleep(10)

driver.find_element(By.CLASS_NAME, 'button__f6b7ccfb8d').click()

# driver.sleep(2)

# <button class="button__f6b7ccfb8d secondary__ed561f3e09" type="button" title="Load More Results" aria-label="Load More Results">Load More Results</button>

driver.quit()


# <button title="Yes, I Accept" aria-label="Yes, I Accept" class="message-component message-button no-children focusable buttons-row sp_choice_type_11" style="opacity: 1; padding: 12px 30px; margin: 10px; border-width: 1px; border-color: rgb(0, 0, 0); border-radius: 0px; border-style: solid; font-size: 16px; font-weight: 700; color: rgb(255, 255, 255); font-family: arial, helvetica, sans-serif; width: auto; background: rgb(0, 0, 0);">Yes, I Accept</button>



# time.sleep(2)

# while True:
#     try:
#         load_more_button = driver.find_element(by=By.CLASS_NAME, value='button__f6b7ccfb8d')
#         load_more_button.click()
#         time.sleep(2)
#     except:
#         break
# full_page_source = driver.page_source
# soup = BeautifulSoup(full_page_source, 'html.parser')

# headlines = soup.find_all('a', class_="headline__3a97424275")

# print(headlines)


# //*[@id="notice"]/div[5]/button[1] - button accept

# //*[@id="notice"]/div[5]/button[1]

# <button class="button__f6b7ccfb8d secondary__ed561f3e09" type="button" 
# title="Load More Results" aria-label="Load More Results">Load More Results</button>

# <a class="headline__3a97424275" href="https://www.bloomberg.com/news/articles/2023-03-17/recession-yes-but-markets-cling-to-hope-crisis-will-be-avoided">Recession, Yes. But Markets Cling to Hope Crisis Will Be Avoided</a>


