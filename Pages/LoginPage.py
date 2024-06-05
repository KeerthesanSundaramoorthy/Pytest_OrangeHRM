from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_locator = (By.XPATH, "//input[@name='username']")
    password_locator = (By.XPATH, "//input[@name='password']")
    login_button_locator = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        self.send_key(*self.username_locator, username)
        self.send_key(*self.password_locator, password)
        self.click(*self.login_button_locator)


        
