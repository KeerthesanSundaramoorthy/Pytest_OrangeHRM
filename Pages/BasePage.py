from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def find(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))
    
    def click(self, by, locator):
        element = self.find(by, locator)
        element.click()

    def send_key(self, by, locator, text):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(text)
