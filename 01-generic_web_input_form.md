## Simple script to automate testing web input forms

In order to test web input forms, you need permission.  You may test the login form located at:  

http://www.nelsontech.blog/Tutorial-SWVV/LogonDemo/login.html

![screen shot of login page](images/loginPage3.png)

### Pre-requisites

In order to run this script, install [Selenium](https://selenium-python.readthedocs.io/installation.html) and [Python](https://www.python.org/downloads/).  Use a [Firefox browser](https://www.mozilla.org/en-US/firefox/)

### How it works

Import the Selenium libraries and import the time library 

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
```
Use the Firefox web driver to run the tests
```
driver = webdriver.Firefox()
```
Set up the test by adding a link to the login webpage
```
driver.get("http://www.nelsontech.blog/Tutorial-SWVV/LogonDemo/login.html")
```
Automate typing the username and the password
```
usr = driver.find_element_by_id("username_field")
pwd = driver.find_element_by_id("password_field")
btn = driver.find_element_by_id("login_button")
```
Automate typing the username and the password
```
usr.send_keys('demo', Keys.ARROW_DOWN)
pwd.send_keys('mode', Keys.ARROW_DOWN)
```
Automate clicking the login button
```
btn.click()
```
Get the results and compare them to the expected results
```
if driver.title == "Welcome":
	print("Test passed")
else:
        print("Test failed ", driver.title)
```
Shut down Firefox
```
driver.quit()
```
Congratulations!  You just automated testing a login form

### Test drive the script

Here's the entire script:

[01_generic_web_input_form.py](code/01_generic_web_input_form.py)

### Resources

[Selenium-Python Read the Docs](https://selenium-python.readthedocs.io/navigating.html)
