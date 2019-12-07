## Using the Page Object Model design pattern to test web input forms

**The Page Object Model is a popular way of organizing tests so they are easier to maintain.**

This example has four scripts:

 - Tests in [loginTest.py](loginTest.py)
 - A Page Object Model in [loginPage.py](loginPage.py)
 - Locators in [locators.py](locators.py)
 - Elements in [element.py](element.py)

### Tests

Import the unittest testing toolkit for constructing and running tests.  Import the Selenium web driver for automating a web browser.  Import the page object model called "loginPage" with code for the login page you are testing.

```
import unittest
from selenium import webdriver
import loginPage
```

Create a testcase by generating a subclass of unittest.TestCase

```
class LoginTest(unittest.TestCase):
    """Test class for login tests"""
    
```
Define a setUp() method to set the driver and the webpage being tested

```
    def setUp(self):
        self.driver = webdriver.Firefox()
        # link to page being tested
        self.driver.get("http://www.nelsontech.blog/Tutorial-SWVV/LogonDemo/login.html")
```
Define tests by defining methods that begin with letters "test".  This informs the test runner that these methods are tests.  Short tests are easier to manage.  For example, this script has four short tests.  The first test checks whether you can logon with a valid username ('demo') and password ('mode').  It starts by making sure you are on the Example Login Page.  It ends by making sure you are logged into the "Welcome" page.
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


    
### Resources

This example was inspired by Baiju Muthukadan, the author of Selenium-Python at https://selenium-python.readthedocs.io/

Learn more about Unittest at https://docs.python.org/3/library/unittest.html
