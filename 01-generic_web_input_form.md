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
Use the "view source" command in the web browser to look at the HTML so you can decide how to find the elements you are testing

```
      <form name="login_form" onsubmit="login(this.username_field.value, this.password_field.value); return false;">
        <table>
          <tr>
            <td><label for="username_field">Username:</label></td>
            <td><input id="username_field" size="30" type="text"></td>
          </tr>
          <tr>
            <td><label for="password_field">Password:</label></td>
            <td><input id="password_field" size="30" type="password"></td>
          </tr>
          <tr>
            <td>&nbsp;</td>
            <td><input id="login_button" type="submit" value="LOGIN"></td>
          </tr>
        </table>
      </form>
```
In this example, the script will type a username and password, then click the login button.  Notice that the input field for username has an id="username_field".  You can find this field by using the find_element_by_id command.
```
usr = driver.find_element_by_id("username_field")
```
The password field has an id of "password_field" and the login button has an id of "login_button".  Looking for ids is the best way to find fields.
```
pwd = driver.find_element_by_id("password_field")
btn = driver.find_element_by_id("login_button")
```
Now that you found the fields, automate typing a valid username and password.  Make sure to move the mouse arrow down after you enter the text
```
usr.send_keys('demo', Keys.ARROW_DOWN)
pwd.send_keys('mode', Keys.ARROW_DOWN)
```
Automate clicking the login button
```
btn.click()
```
Check the results and compare them to the expected results.  In this case, you should see the Welcome page which has a title of "Welcome".  Try changing the username or password.  Then, this test should fail because the script could not login.  When this test fails, the result is a "Test failed" message along with the title of the webpage it found.
```
if driver.title == "Welcome":
	print("Test passed")
else:
        print("Test failed ", driver.title)
```
Shut down Firefox to cleanup your test environment
```
driver.quit()
```
Congratulations!  You just automated testing a login form

### Test drive the script

Here's the entire script:

[01_generic_web_input_form.py](code/01_generic_web_input_form.py)

### Resources

[Selenium-Python Read the Docs](https://selenium-python.readthedocs.io/navigating.html)
