# Test Case: Verify search works

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open website page
driver.get('https://www.target.com/')
search_word = "tea"

# Search for tea
driver.find_element(By.ID, "search").send_keys(search_word)
driver.find_element(By.XPATH, "//*[@data-test='@web/Search/SearchButton']").click()

sleep(10)

# Verify search worked
# assert driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']//span[contains(text(), 'tea')]"), \
#     f"Expected word {search_word} not found in search results"
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']/span[contains(text(), 'for “{}”')]".format(search_word))
assert search_word in actual_text, f'Expected word "{search_word}" not found in search results: {actual_text}'


print("Test case passed")
driver.quit()
