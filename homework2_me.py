# My test cases

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

# # Verify GiftCards from side navigation clickable.
# # Click SignIn button
# driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
#
# # Click GiftCards from side navigation
# driver.find_element(By.XPATH, "//*[@data-test='accountNav-giftCards']//*[text()='Gift Cards']").click()
sleep(10)
# Verify AboutUs in footer visible. Verify all links under AboutUs clickable.
# driver.find_element(By.XPATH, "//*[@data-test='@web/component-footer/PrimarySection'][text()='About Us']")        # "//div//*[text()='About Us']"
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-test='resultsHeading']//a")))
links = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']//a")
for link in links:
    link.click()
    driver.back()

print("Test case passed")
driver.quit()
