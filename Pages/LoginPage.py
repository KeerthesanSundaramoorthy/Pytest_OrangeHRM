from Pages.BasePage import BasePage
import time
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    username_locator = "//input[@name='username']"
    password_locator = "//input[@name='password']"
    login_button_locator = "//button[@type='submit']"

    def login(self,username,password):
        self.send_key(By.XPATH,self.username_locator,username)
        self.send_key(By.XPATH,self.password_locator,password)
        self.click(By.XPATH,self.login_button_locator)
        time.sleep(5)
