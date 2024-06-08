"""Author: Keerthesan (Expleo)"""
from selenium.webdriver.common.by import By
from Pages.JobPage import JobPage

class EmploymentPage(JobPage):

    def __init__(self, driver):
        super().__init__(driver)

    employment_xpath = "(//ul[@class='oxd-dropdown-menu']//li)[3]"
    employ_textbox_xpath = "//div[@class='oxd-input-group__label-wrapper']/following-sibling::div//input"
    assert_xpath = "(//div[@class='oxd-toast-content oxd-toast-content--success']//p)[2]"

    def employ_status(self):

        """Navigate to the employment status section."""

        #admin = self.find(By.CSS_SELECTOR,self.admin_css)
        self.click(By.CSS_SELECTOR,self.admin_css)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"):
                #job = self.find(By.XPATH,self.job_xpath)
                self.click(By.XPATH,self.job_xpath)
                self.click(By.XPATH,self.employment_xpath)

    def add_employ_status(self,status):

        """Adds the new employment status."""

        self.send_key(By.XPATH,self.employ_textbox_xpath,status)

    def assert_employ(self):

        """Assert the success message after adding employment status."""
        
        try:
            actual = "Successfully Saved"
            expected = self.find(By.XPATH,self.assert_xpath).text
            assert actual.__eq__(expected), f"Assertion failed: expected text is '{expected}', but the actual text is '{actual}'"
            return True
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False 