import unittest
from selenium import webdriver
import loginPage

class LoginTest(unittest.TestCase):
    """Test class for login tests"""

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

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
