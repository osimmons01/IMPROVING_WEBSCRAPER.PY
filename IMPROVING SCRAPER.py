from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import random


driver = webdriver.Chrome()

try:
    url = "https://www.reddit.com/r/Drumkits/"
    driver.get(url)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    soup = BeautifulSoup(driver.page_source,'html.parser')

    links = soup.find_all('a', href=True)

    drive_links = [link['href'] for link in links if 'drive.google.com' in link['href']]

    if drive_links:

        print(random.choice(drive_links))
    else:
        print("No Google Drive links found.")
finally:
    driver.quit()