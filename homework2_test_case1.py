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

# # 1. Practice with locators.
# # Given webpage:
# driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
# sleep(15)
#
# # Amazon logo
# driver.find_element(By.XPATH, "//i[@class='a-icon a-logo']")
#
# # Email field
# driver.find_element(By.ID, "ap_email")
#
# # Continue button
# driver.find_element(By.ID, "continue")
#
# # Conditions of use link
# driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(), 'Conditions of Use')]")
# driver.find-element(By.XPATH, "//a[contains(@href, 'ap-signin_notification_condition-of_use')]")

# # Privacy Notice link
# driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[.='Privacy Notice']")
#
# # Need help link
# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt'][normalize-space()='Need help?']")
#
# # Forgot your password link
# driver.find_element(By.XPATH, "//*[contains(text(), 'Forgot your password?')")
#
# # Other issues with Sign-In link
# driver.find_element(By.ID, "ap-other-signin-issues-link")
#
# # Create your Amazon account button
# driver.find_element(By.XPATH, "//*[contains(text(), 'Create your Amazon account')]")

# ____________________________________________________________________________________________
# Test Case: Users can navigate to SignIn page

driver.maximize_window()

# Open website page
driver.get('https://www.target.com/')

# Click SinIn button
driver.find_element(By.XPATH, "//*[@aria-label='Account, sign in']").click()
sleep(20)

# Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//*[contains(text(), 'Sign in')]").click()
sleep(20)

# Verify SignIn page opened:
# “Sign into your Target account” text is shown
expected_text = "Sign into your Target account"
actual_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Sign into your Target account')]").text
assert expected_text in actual_text, f"Expected text {expected_text} not in {actual_text}"

# SignIn button is shown
assert driver.find_element(By.ID, 'login').is_displayed(), "Login button not appear"
# or (But the upper is more correct)
# expected_button_text = "Sign in"
# actual_button_text = driver.find_element(By.XPATH, "//button[@id='login']").text
# assert expected_button_text in actual_button_text, f"Expected text {expected_button_text} not in {actual_button_text}"

print("Test case passed")
driver.quit()

______________________________________________________________________________________________________
