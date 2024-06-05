from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Utility import utility_file

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    save_button_xpath = "(//p[@class='oxd-text oxd-text--p orangehrm-form-hint']//following-sibling::button)[2]"
    add_button_xpath = "//button[@type='button'][@class='oxd-button oxd-button--medium oxd-button--secondary']"

    def find(self, by, locator):
        return self.wait.until(ec.visibility_of_element_located((by,locator)))
    
    def click(self,locator):
        self.action.key_down(Keys.CONTROL).click(locator).key_up(Keys.CONTROL).perform()
        #self.driver.execute_script("arguments[0].click()",locator)

    def send_key(self, locator, text):
        #self.driver.execute_script("arguments[0].value = arguments[1];", locator, text)
        #locator.send_keys(text)
        self.driver.execute_script("arguments[0].focus(); arguments[0].value = arguments[0].value + '" + text + "'; arguments[0].dispatchEvent(new Event('input'));", locator)

    def add(self):
        add = self.find(By.XPATH,self.add_button_xpath)
        self.click(add)

    def click_save(self):
        save_but = self.find(By.XPATH,self.save_button_xpath)
        self.click(save_but)

    def valid_login(self):
        from Pages.LoginPage import LoginPage  # Local import to avoid circular dependency
        login = LoginPage(self.driver)  # Object reference
        username = utility_file.get_config("valid login details", "username")
        password = utility_file.get_config("valid login details", "password")
        login.login(username, password)


        