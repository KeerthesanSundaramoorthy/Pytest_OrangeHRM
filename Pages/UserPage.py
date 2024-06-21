"""Author: Keerthesan (Expleo)"""
import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException, JavascriptException
from selenium.webdriver.support import expected_conditions as ec


class UserPage(BasePage):

    def __init__(self, driver):
       super().__init__(driver)

    admin_css = "a[href='/web/index.php/admin/viewAdminModule']"
    user_man_xpath = "(//div[@class='oxd-topbar-body']//span)[1]"
    users_xpath = "//ul[@class='oxd-dropdown-menu']//a"
    username_xpath = "(//div[@class='oxd-grid-item oxd-grid-item--gutters']//input)[1]"
    user_role_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1]"
    ess_xpath = "//span[text()='ESS']"
    employee_name_xpath = "//input[@placeholder='Type for hints...']"
    status_xpath = "(//div[@class='oxd-select-text oxd-select-text--active']//div)[3]"
    enabled_xpath = "//span[text()='Enabled']"
    search_button_xpath = "//button[text()=' Search ']"
    admin_role_xpath = "//span[text()='Admin']"
    assert_user_xpath = "(//div[@class='oxd-table-header']//div)[4]"

    def user_management(self):

        """Navigate to user management section"""

        self.click(By.CSS_SELECTOR,self.admin_css)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"):
                self.click(By.XPATH,self.user_man_xpath)
                self.click(By.XPATH,self.users_xpath)

    def username(self,user):

        """Enters username in the corresponding text box."""
        
        self.send_key(By.XPATH,self.username_xpath,user)

    def ess_userrole(self):

        """Selects the ESS user role"""
        
        self.click(By.XPATH,self.user_role_xpath)
        ess = self.wait.until(ec.element_to_be_clickable((By.XPATH,self.ess_xpath)))
        ess.click()
        
    def admin_userrole(self):

        """Selects the Admin user role"""
        
        self.click(By.XPATH,self.user_role_xpath)
        admin = self.wait.until(ec.element_to_be_clickable((By.XPATH,self.admin_role_xpath)))
        admin.click()
        time.sleep(2)

    def employee_name(self,emp_name):

        """Enters employee name in the corresponding text box."""

        self.send_key(By.XPATH,self.employee_name_xpath,emp_name)
        emp = self.wait.until(ec.element_to_be_clickable((By.XPATH,"//span[text()='FName Mname LName']")))
        emp.click()

    def select_status(self):

        """Selects the user status"""

        self.click(By.XPATH,self.status_xpath)
        enabled = self.wait.until(ec.element_to_be_clickable((By.XPATH,self.enabled_xpath)))
        enabled.click()

    def search(self):

        """Clicks on search button"""

        try:
            self.click(By.XPATH, self.search_button_xpath)
        
        except TimeoutException as e:
            print(f"TimeoutException: Element {self.search_button_xpath} not clickable after waiting. {e}")
        
        except NoSuchElementException as e:
            print(f"NoSuchElementException: Element {self.search_button_xpath} not found. {e}")
        
        except Exception as e:
            print(f"Exception occurred while trying to click element {self.search_button_xpath}. {e}")

    def search_assert(self):

        """Asserts the user search"""

        try:
            return self.find(By.XPATH, self.assert_user_xpath).is_displayed()
    
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

