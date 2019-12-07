## Simple script to automate testing web input forms

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("http://www.nelsontech.blog/Tutorial-SWVV/LogonDemo/login.html")

usr = driver.find_element_by_id("username_field")
pwd = driver.find_element_by_id("password_field")
btn = driver.find_element_by_id("login_button")

usr.send_keys('demo', Keys.ARROW_DOWN)
pwd.send_keys('mode', Keys.ARROW_DOWN)
btn.click()

if driver.title == "Welcome":
	print("Test passed")
else:
        print("Test failed ", driver.title)

driver.quit()
```
