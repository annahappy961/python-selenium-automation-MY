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

# open the url
driver.get('https://www.google.com/')

driver.find_element(By.ID, 'search').send_keys('coffe')

# click on Search btn
driver.find_elementa(By.XPath, '').click()
# wait for 6 sec
sleep(6)

actual_text = driver.find_element(By.XPath, "")

# populate search field
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('cat')

# wait for 4 sec
sleep(4)