from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set the path to the browser driver (ChromeDriver)
chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'

# Set browser options (optional)
chrome_options = Options()
# chrome_options.add_argument('--headless')  # Runs the browser in headless mode

# Create a browser service
service = Service(chrome_driver_path)

# Launch the browser
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.bloomberg.com/search?query=AAPL'

driver.get(url)
time.sleep(15)

# Click the "Load More" button
load_more_button = driver.find_element_by_css_selector("button.button__f6b7ccfb8d.secondary__ed561f3e09")
load_more_button.click()

# Wait for additional data to load
time.sleep(10)

# Get the full page source
full_page_source = driver.page_source

# Now you can continue processing the page or use BeautifulSoup to parse the data
