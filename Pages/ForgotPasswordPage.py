from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    forgotPassword_locator = (By.XPATH, "//div[@class='orangehrm-login-forgot']//p")
    username_locator = (By.XPATH, "//input[@name='username']")
    resetPassword_locator = (By.XPATH, "//button[text()=' Reset Password ']")
    cancelPassword_locator= (By.XPATH, "//button[text()=' Cancel ']")

    def forgotPassword(self, username):
        self.click(*self.forgotPassword_locator)
        self.send_key(*self.username_locator, username)
        self.click(*self.resetPassword_locator)

    def forgotPassword_cancel(self, username):
        self.click(*self.forgotPassword_locator)
        self.send_key(*self.username_locator, username)
        self.click(*self.cancelPassword_locator)
   


        
