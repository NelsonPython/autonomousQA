## Using the Page Object Model design pattern to test web input forms

**The Page Object Model is a popular way of organizing tests so they are easier to maintain.**  This example has four scripts:

 - Testcases in [loginTest.py](code/02-generic-pom-example/loginTest.py)
 - A Page Object Model for the login page in [loginPage.py](code/02-generic-pom-example/loginPage.py)
 - Locators in [locators.py](code/02-generic-pom-example/locators.py)
 - Elements in [element.py](code/02-generic-pom-example/element.py)
 
### Pre-requisites

In order to test a web input form, you need permission.  For purposes of running this script, you may test the login form located at:  http://www.nelsontech.blog/Tutorial-SWVV/LogonDemo/login.html

![screen shot of login page](images/loginPage3.png)

In order to run this script, make sure [Python](https://www.python.org/downloads/) is installed.  Install [Selenium for Python](https://selenium-python.readthedocs.io/installation.html).  Use a [Firefox browser](https://www.mozilla.org/en-US/firefox/)

### Testcases

Import the unittest testing toolkit for constructing and running tests.  Import the Selenium web driver for automating a web browser.  Import the "loginPage" script with code specifically for the login page you will be testing.

```
import unittest
from selenium import webdriver
import loginPage
```

Create a testcase called "LoginTest" by generating a subclass of unittest.TestCase

```
class LoginTest(unittest.TestCase):   
```
Define a setUp method to set the web driver and the webpage to be tested

```
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.nelsontech.blog/Tutorial-SWVV/LogonDemo/login.html")
```
Make sure all your test methods begin with "test". This informs the test runner that these methods are tests. Short tests are easier to manage. For example, this script has four short tests. The first test checks whether you can logon with a valid username ('demo') and password ('mode'). It starts by making sure you are on the "Example Login Page". It ends by checking that you are logged into the "Welcome" page.
```
    def test_valid_login(self):
        """
        tests valid login
        """
        main_page = loginPage.MainPage(self.driver)
        self.assertEqual(main_page.is_title_matches(), "Example Login Page")
        main_page.fill_in_credentials('demo','mode')
        main_page.click_login_button()
        self.assertEqual(main_page.is_title_matches(), "Welcome")
```
The next two tests check whether you get an error if you try to logon with the wrong username or password.  Notice, that we are not expecting a "Welcome" message.  We are expecting a "Login error" message.
```
    def test_invalid_username(self):
        """
        tests invalid username
        """
        main_page = loginPage.MainPage(self.driver)
        self.assertEqual(main_page.is_title_matches(), "Example Login Page")
        main_page.fill_in_credentials('test','mode')
        main_page.click_login_button()
        self.assertEqual(main_page.is_title_matches(), "Login error")

    def test_valid_password(self):
        """
        tests valid password
        """
        main_page = loginPage.MainPage(self.driver)
        self.assertEqual(main_page.is_title_matches(), "Example Login Page")
        main_page.fill_in_credentials('demo','invalid')
        main_page.click_login_button()
        self.assertEqual(main_page.is_title_matches(), "Login error")
```
You can also automate cybersecurity tests.  In this example, we are attempting to inject special SQL code that may give us access to the database if the webpage security is not set properly.  
```
    def test_SQL_injection(self):
        """
        cybersecurity test for SQL injection
        """
        main_page = loginPage.MainPage(self.driver)
        self.assertEqual(main_page.is_title_matches(), "Example Login Page")
        main_page.fill_in_credentials("'or''='",'mode')
        main_page.click_login_button()
        self.assertEqual(main_page.is_title_matches(), "Login error")
```
Define a tearDown method to clean up after you finish testing
```
    def tearDown(self):
        self.driver.close()
```
Use this Python convention to start your script.  [Read more about these special variables __name__ and __main__](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
```
if __name__ == "__main__":
    unittest.main()
```    

### Login Page Object Model

This script has code specifically for the login page. Generic elements are stored in the element.py script. Locators are stored in the locators.py script. Import the BasePageElement from element.py and the MainPageLocators from locators.py. Import the Selenium Keys library so you can move the mouse arrow.

```
from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
```
The BasePage object contains generic information such as the web driver
```
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
```
The MainPage inherits from the BasePage
```
class MainPage(BasePage):

```
Define methods for each test.  Use names that describe the purpose of the test.  The is_title_matches method gets the page title so you can make sure you are testing the correct page
```
    def is_title_matches(self):
        """ gets page title"""
        return self.driver.title
```
The fill_in_credentials method finds the username and password fields and types in the username and password for the testcase.
Use the "view source" command in the web browser to look at the HTML so you can decide how to find the elements you are testing.
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
    def fill_in_credentials(self,username,password):
        """  gets fields for credentials and types in test credentials """
        usr = self.driver.find_element_by_id("username_field")
```
The password field has an id of "password_field".  Looking for ids is the best way to find fields.
```
        pwd = self.driver.find_element_by_id("password_field")
        usr.send_keys(username,Keys.ARROW_DOWN)
        pwd.send_keys(password,Keys.ARROW_DOWN)
```
The click_login_button method clicks the login button
```
    def click_login_button(self):
        """attempts login"""
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()
```
### Locators

Locators are used to find elements on a web page such as the login button.  In this example, import the Selenium web driver common library so you can use the "By" locators.  
```
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
```
In the browser, you can right mouse click on the Login.html page and select "view source" to see the HTML.  Notice that the login button has an id="login_button".
```
<input id="login_button" type="submit" value="LOGIN">
```
You can use this ID to find the login button
```    
    LOGIN_BUTTON = (By.ID, 'login_button')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass
```
 
 ### Elements
You can use the element.py script to get or to set a webpage element

```
from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
```
 
### Resources

This example was inspired by Baiju Muthukadan, the author of Selenium-Python at https://selenium-python.readthedocs.io/

Learn more about Unittest at https://docs.python.org/3/library/unittest.html
