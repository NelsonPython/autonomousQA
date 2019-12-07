## Using the Page Object Model design pattern to test web input forms

**The Page Object Model is a popular way of organizing tests so they are easier to maintain.**

This example has four scripts:

1.  tests
2.  page object model
3.  locators
4.  elements


### Tests

Import unittest, the Selenium web driver, and a page object model called loginPage

```
import unittest
from selenium import webdriver
import loginPage
```
Create a testcase by generating a subclass of unittest.TestCase.  Define tests by defining methods that begin with letters "test".  This informs the test runner that these methods are tests.  

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

    def test_valid_login(self):
        """
        tests valid login
        """
        main_page = loginPage.MainPage(self.driver)
        self.assertEqual(main_page.is_title_matches(), "Example Login Page")
        main_page.fill_in_credentials('demo','mode')
        main_page.click_login_button()
        self.assertEqual(main_page.is_title_matches(), "Welcome")

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

```
if __name__ == "__main__":
    unittest.main()
```    
    
### Resources

This example was inspired by Baiju Muthukadan, the author of Selenium-Python at https://selenium-python.readthedocs.io/

Learn more about Unittest at https://docs.python.org/3/library/unittest.html
