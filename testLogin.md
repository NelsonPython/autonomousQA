
# Automating your login tests

**This script automates testing the error message that appears when a user enters the wrong password**

### Pre-requisites

In order to run this script, install Selenium and Python

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
To use this sample, you will need Firefox
```
driver = webdriver.Firefox()
```
The website to be tested in this example is the I3 marketplace login
```
driver.get("http://3.17.183.219:8000")
```
Set up the first test with a good user name and an bad password
```
print("TEST 1 - invalid login")

usr = "Testuser"
pwd = "invalid"
```
Automate typing the username and password
```
username = driver.find_element_by_id('inputEmail')
username.send_keys(usr)
password = driver.find_element_by_id('inputPassword')
password.send_keys(pwd)
```
Automate clicking the Login button
```
driver.find_element_by_xpath('//button[@type="submit"]').click()
```
Take a screen capture

```
driver.save_screenshot('Test1.png')
```
![](images/Test1.png)

Wait 2 seconds so you can see what happens
```
time.sleep(2)
```
the expected result is

```
<p class="text-danger">Invalid username/password!</p>
```
Get the test result and compare it to the expected result.  If they match, then print a message saying the test passed.  If they do not match, then print the test results

```
res = driver.find_element_by_tag_name('p')
if res.text == 'Invalid username/password!':
	print("Test Passed with expected output: ", res.text)
else:
    print(res.text)
```
Shut down the browser
```
driver.quit()
```

### Resources

[Selenium-python Read the Docs](https://selenium-python.readthedocs.io/navigating.html)
