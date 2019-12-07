## Simple script to automate testing web input forms

In order to test a web input form, you need permission.  For purposes of running this script, you may test the login form located at:  http://www.nelsontech.blog/Tutorial-SWVV/LogonDemo/login.html

![screen shot of login page](images/loginPage3.png)

In order to run this script, make sure [Python](https://www.python.org/downloads/) is installed.  Install [Selenium for Python](https://selenium-python.readthedocs.io/installation.html).  Use a [Firefox browser](https://www.mozilla.org/en-US/firefox/)

### How it works

Import the Selenium libraries

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```
Use the Firefox web driver to automate the web browser
```
driver = webdriver.Firefox()
```
Tell the script which website to test
```
driver.get("http://www.nelsontech.blog/Tutorial-SWVV/LogonDemo/login.html")
```
Get the username and the password field names
```
usr = driver.find_element_by_id("username_field")
pwd = driver.find_element_by_id("password_field")
btn = driver.find_element_by_id("login_button")
```
Automate typing a valid username and password
```
usr.send_keys('demo', Keys.ARROW_DOWN)
pwd.send_keys('mode', Keys.ARROW_DOWN)
```
Automate clicking the login button
```
btn.click()
```
Get the results and compare them to the expected results.  In this case, you should see the Welcome page.  Try changing the username or password to see the error page.
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
