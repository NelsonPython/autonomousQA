from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    """ setup """

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """page actions"""

    def is_title_matches(self):
        """ gets page title"""
        return self.driver.title

    def fill_in_credentials(self,username,password):
        """  gets fields for credentials and types in test credentials """
        usr = self.driver.find_element_by_id("username_field")
        pwd = self.driver.find_element_by_id("password_field")
        usr.send_keys(username,Keys.ARROW_DOWN)
        pwd.send_keys(password,Keys.ARROW_DOWN)

    def click_login_button(self):
        """attempts login"""
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()
