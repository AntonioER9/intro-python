from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detatch', True)
browser = webdriver.Chrome(options=options)

browser.implicitly_wait(5)
browser.get('https://www.google.com')

link = browser.find_element(By.LINK_TEXT,"Sign in")
link.click()

user_input = browser.find_element(By.ID,"login_field")
pass_input = browser.find_element(By.ID,"password")


user_input.send_keys("user")
pass_input.send_keys("pass")
pass_input.send_keys(Keys.RETURN)

profile = browser.find_element(By.CLASS_NAME,"user-profile-link")
label = profile.get_attribute("aria-label")

assert "AntonioER9" in label

browser.quit()