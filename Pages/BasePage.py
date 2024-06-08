from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, JavascriptException
from Utility import utility_file

class BasePage:

    """BasePage class in the base page contains the method for clicking,send keys and finding an element ,which the child class inherits."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    save_button_xpath = "(//p[@class='oxd-text oxd-text--p orangehrm-form-hint']//following-sibling::button)[2]"
    add_button_xpath = "//button[@type='button'][@class='oxd-button oxd-button--medium oxd-button--secondary']"

    def find(self, by, locator):

        """ This method finds and returns the web element identified by the specified locator."""

        try:
            return self.wait.until(ec.visibility_of_element_located((by,locator)))
        
        except TimeoutException as e:
            print(f"TimeoutException: Element {locator} not visible after waiting. {e}")

        except NoSuchElementException as e:
            print(f"NoSuchElementException: Element {locator} not found. {e}")

        except Exception as e:
            print(f"Exception occurred while trying to find element {locator}. {e}")
            return None
    
    def click(self,by,locator):

        """This method clicks on the web element identified by the specified locator."""
        
        try:
            element = self.find(by, locator)
            self.action.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
            # self.driver.execute_script("arguments[0].click()", locator)
        
        except TimeoutException as e:
            self.handle_exception("TimeoutException", locator, e)
        
        except NoSuchElementException as e:
            self.handle_exception("NoSuchElementException", locator, e)
        
        except Exception as e:
            self.handle_exception("Exception", locator, e)

    def handle_exception(self, exception_name, locator, e):
        
        """This method handles exceptions encountered during element interaction."""
        
        print(f"{exception_name}: Element {locator} encountered an exception: {e}")

    def send_key(self, by, locator, text):

        """This method sends keys to the web element identified by the specified locator."""
        
        try:
            #self.driver.execute_script("arguments[0].value = arguments[1];", locator, text)
            #locator.send_keys(text)
            element = self.find(by,locator)
            self.driver.execute_script("arguments[0].focus(); arguments[0].value = arguments[0].value + '" + text + "'; arguments[0].dispatchEvent(new Event('input'));", element)

        except TimeoutException as e:
            print(f"TimeoutException: Element {locator} not found after waiting. {e}")

        except NoSuchElementException as e:
            print(f"NoSuchElementException: Element {locator} not found. {e}")

        except JavascriptException as e:
            print(f"JavascriptException: Issue executing JavaScript for {locator}. {e}")
            
        except Exception as e:
            print(f"Exception occurred while trying to send keys to element {locator}. {e}")

    def add(self):

        """This method clicks on the 'Add' button."""
        
        #add = self.find(By.XPATH,self.add_button_xpath)
        self.click(By.XPATH,self.add_button_xpath)

    def click_save(self):

        """This method clicks on the 'Save' button."""
        
        #save_but = self.find(By.XPATH,self.save_button_xpath)
        self.click(By.XPATH,self.save_button_xpath)

    def valid_login(self):
        
        """Performs a valid login using credentials retrieved from the configuration file."""
        
        from Pages.LoginPage import LoginPage  # Local import to avoid circular dependency
        login = LoginPage(self.driver)  # Object reference
        username = utility_file.get_config("valid login details", "username")
        password = utility_file.get_config("valid login details", "password")
        login.login(username, password)