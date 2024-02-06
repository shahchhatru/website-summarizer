from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the URL of the website you want to scrape

url = "https://kathmandupost.com/national/2024/02/06/nepal-proposes-tariff-for-electricity-export-to-bangladesh"

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Open the URL in the webdriver
driver.get(url)

# Wait for the page to load completely
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Extract all the information from the website
all_elements = driver.find_elements(By.XPATH, "//*")

for element in all_elements:
    try:
        print(element.text)
    except UnicodeEncodeError:
        # If an error occurs, try to encode the text using UTF-8
        print(element.text.encode('utf-8'))

# Close the webdriver
driver.quit()
