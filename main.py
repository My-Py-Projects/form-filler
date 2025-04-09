import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Load environment variables
load_dotenv()

# URLs
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
forms_url = os.getenv("FORMS_URL")

# Requests + BS
response = requests.get(zillow_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Create addresses list
addresses_elems = soup.select("address")
addresses = [address.text.strip() for address in addresses_elems]

# Create prices list
prices_elems = soup.select('span.PropertyCardWrapper__StyledPriceLine')
prices = [
    price.text.strip().replace('/mo', '').replace('+', '')
    for price in prices_elems
]

# Create links list
links_elems = soup.select('.property-card-link')
links = [link['href'] for link in links_elems]

# Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(f"{forms_url}")

# Fill up the forms
for address, price, link in zip(addresses, prices, links):
    driver.get(forms_url)
    time.sleep(2)

    first_question = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    second_question = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third_question = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    first_question.send_keys(address)
    second_question.send_keys(str(price))
    third_question.send_keys(link)

    send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    send_button.click()
    time.sleep(2)