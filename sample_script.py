# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# # open the url
# driver.get('https://www.google.com/')
#
# # populate search field
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('cat')
#
# # wait for 4 sec
# sleep(4)
#
# # click search button
# driver.find_element(By.NAME, 'btnK').click()
#
# # verify search results
# assert 'cat' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
# print('Test Passed')
#
# driver.quit()

number = 1597

digit_1 = number % 10
number = number // 10

digit_2 = number % 10
number = number // 10

digit_3 = number % 10
number = number // 10

digit_4 = number % 10


print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)
