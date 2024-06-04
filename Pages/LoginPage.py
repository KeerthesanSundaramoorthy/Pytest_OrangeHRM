import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
       super().__init__(driver)   

    username_name = "username"
    password_name = "password"
    login_button_xpath = "//button[@type='submit']"

    def login(self,username,password):
        uname = self.find(By.NAME,self.username_name)
        self.send_key(uname,username)
        passw = self.find(By.NAME,self.password_name)
        self.send_key(passw,password)
        login_but = self.find(By.XPATH,self.login_button_xpath)
        self.click(login_but)