from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def find(self, by, locator):
        return self.wait.until(ec.visibility_of_element_located((by,locator)))
    
    def click(self,locator):
        self.action.key_down(Keys.CONTROL).click(locator).key_up(Keys.CONTROL).perform()

    def send_key(self, locator, text):
        self.driver.execute_script("arguments[0].value = arguments[1];", locator, text)


        