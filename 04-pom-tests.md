## Using the Page Object Model design pattern to automate I3 login tests

```
import unittest
from selenium import webdriver
import loginPage

class LoginTest(unittest.TestCase):
    """Test class for login tests"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        # link to page being tested
        self.driver.get("http://3.17.183.219:8000")

    def test_invalid_username(self):
        """
        tests invalid username
        """
        main_page = loginPage.MainPage(self.driver)
        self.assertEqual(main_page.is_title_matches(), "I3 Marketplace | Login")
        main_page.fill_in_credentials('test','mode')
        main_page.click_login_button()
        self.assertEqual(main_page.login_message(), 'Invalid username/password!')

    def test_SQL_injection(self):
        """
        cybersecurity test for SQL injection
        """
        main_page = loginPage.MainPage(self.driver)
        self.assertEqual(main_page.is_title_matches(), "I3 Marketplace | Login")
        main_page.fill_in_credentials("'or''='","'or''='")
        main_page.click_login_button()
        self.assertEqual(main_page.login_message(), 'Invalid username/password!')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```
