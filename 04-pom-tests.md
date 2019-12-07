## Using the Page Object Model design pattern to automate I3 login tests

**The Page Object Model is a popular way of organizing tests so they are easier to maintain.**  This example has four scripts:

 - Testcases in [loginTest.py](code/04-simple-pom-example/loginTest.py)
 - A Page Object Model for the login page in [loginPage.py](code/04-simple-pom-example/loginPage.py)
 - Locators in [locators.py](code/04-simple-pom-example/locators.py)
 - Elements in [element.py](code/04-simple-pom-example/element.py)

### Testcases

Import the unittest testing toolkit for constructing and running tests.  Import the Selenium web driver for automating a web browser.  Import the page object model called "loginPage" with code for the login page you are testing.

```
import unittest
from selenium import webdriver
import loginPage
```
Create a testcase called LoginTest by generating a subclass of unittest.TestCase
```
class LoginTest(unittest.TestCase):
    """Test class for login tests"""
```
Define a setUp() method to set the driver and the webpage being tested

```
    def setUp(self):
        self.driver = webdriver.Firefox()
        # link to page being tested
        self.driver.get("http://3.17.183.219:8000")
```
Define tests by defining methods that begin with letters "test".  This informs the test runner that these methods are tests.  Short tests are easier to manage.  For example, this script has four short tests.  The first test checks whether you can logon with a valid username ('demo') and password ('mode').  It starts by making sure you are on the Example Login Page.  It ends by making sure you are logged into the "Welcome" page.
```
    def test_invalid_username(self):
        """
        tests invalid username
        """
        main_page = loginPage.MainPage(self.driver)
        self.assertEqual(main_page.is_title_matches(), "I3 Marketplace | Login")
        main_page.fill_in_credentials('test','mode')
        main_page.click_login_button()
        self.assertEqual(main_page.login_message(), 'Invalid username/password!')
```
You can also automate cybersecurity tests.  In this example, we are attempting to inject special SQL code that may give us access to the database if the webpage security is not set properly.  
```
    def test_SQL_injection(self):
        """
        cybersecurity test for SQL injection
        """
        main_page = loginPage.MainPage(self.driver)
        self.assertEqual(main_page.is_title_matches(), "I3 Marketplace | Login")
        main_page.fill_in_credentials("'or''='","'or''='")
        main_page.click_login_button()
        self.assertEqual(main_page.login_message(), 'Invalid username/password!')
```
Define a tearDown() method to clean up after you finish testing
```
    def tearDown(self):
        self.driver.close()
```
Use this Python convention to start your script.  [Read more about these special variables](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
```
if __name__ == "__main__":
    unittest.main()
```

### Page object model for the I3 marketplace login

This script has code specifically for the login page.

Generic elements are stored in the element.py script.  Locators are stored in the locators.py script.  Import these two scripts.  And import the Selenium Keys library so you can move the mouse arrow down.

```
from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
```
The BasePage object contains generic information such as the web driver
```
class BasePage(object):
    """ setup """

    def __init__(self, driver):
        self.driver = driver
```
The MainPage inherits from the BasePage
```
class MainPage(BasePage):
    """page actions"""
```
Define methods for each test.  The is_title_matches method gets the page title so you can make sure you are testing the correct page
```
    def is_title_matches(self):
        """ gets page title"""
        return self.driver.title
```
The fill_in_credentials method finds the username and password fields and types in the username and password for the testcase.  
```
    def fill_in_credentials(self,username,password):
        """  gets fields for credentials and types in test credentials """
        usr = self.driver.find_element_by_id("inputEmail")
        pwd = self.driver.find_element_by_id("inputPassword")
        usr.send_keys(username,Keys.ARROW_DOWN)
        pwd.send_keys(password,Keys.ARROW_DOWN)
```
The click_login_button method clicks the login button
```
    def click_login_button(self):
        """attempts login"""
        element = self.driver.find_element(*MainPageLocators.I3_LOGIN_BUTTON)
        element.click()
```
This login form writes a message when the login fails.  This message is in a paragraph tag so find the tag_name of 'p'
```
    def login_message(self):
        return self.driver.find_element_by_tag_name('p').text
```

### Locators

Use the locators.py script from example 2 and add a locator for the I3_LOGIN_BUTTON.  This button does not have an ID so use XPATH to find a button in an input form with a type of "submit".
```
class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    LOGIN_BUTTON = (By.ID, 'login_button')
    I3_LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
```
