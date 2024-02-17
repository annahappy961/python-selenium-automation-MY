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

driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=BR7KB6MHJJFHGWABXNVM&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
sleep(5)

# Amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")

# Creat account text
driver.find_element(By.XPATH, "//*[contains(text(), 'Create account')]")

# Your name field
driver.find_element(By.ID, "ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# Mobile number or email field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# Password field
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Passwords must be at least 6 characters box
driver.find_element(By.CSS_SELECTOR,".a-alert-inline-info")

# Re-enter password field
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# Continue button
driver.find_element(By.CSS_SELECTOR, "#continue")

# Conditions of Use link
driver.find_element(By.CSS_SELECTOR, "[href*='condition']")

# Privacy Notice link
driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy']")

# SignIn link
driver.find_element(By.CSS_SELECTOR, "[href*='signin']")
