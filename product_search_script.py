from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()


# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# explicit wait
driver.wait = WebDriverWait(driver, 10)

driver.get('https://www.target.com/')
search_word = 'coffee'

# Input search word
driver.find_element(By.ID, 'search').send_keys(search_word)

# Click on search btn
# driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
# driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='@web/Search/SearchButton']"))).click()
BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
driver.wait.until(EC.element_to_be_clickable(BTN)).click()


# Verify search worked:
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
assert search_word in actual_text, f'Expected word {search_word} not in {actual_text}'

print('Test case passed')
driver.quit()
