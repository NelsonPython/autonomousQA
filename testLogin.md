
# selenium-python.readthedocs.io/navigating.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

# website to be tested
driver.get("http://3.17.183.219:8000")

print("TEST 1 - invalid login")

usr = "Testuser"
pwd = "invalid"

username = driver.find_element_by_id('inputEmail')
username.send_keys(usr)
password = driver.find_element_by_id('inputPassword')
password.send_keys(pwd)
driver.find_element_by_xpath('//button[@type="submit"]').click()
driver.save_screenshot('Test1.png')
time.sleep(2)
#Expected result:  <p class="text-danger">Invalid username/password!</p>
res = driver.find_element_by_tag_name('p')
if res.text == 'Invalid username/password!':
	print("Test Passed with expected output: ", res.text)
else:
    print(res.text)
driver.quit()
