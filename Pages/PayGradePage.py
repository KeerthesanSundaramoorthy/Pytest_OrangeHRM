"""Author: Keerthesan (Expleo)"""
from selenium.webdriver.common.by import By
from Pages.JobPage import JobPage

class PayGradePage(JobPage):
    
    def __init__(self, driver):
       super().__init__(driver)

    job_xpath = "(//div[@class='oxd-topbar-body']//span)[2]"
    pay_grade_xpath = "(//ul[@class='oxd-dropdown-menu']//li)[2]"
    name_textbox_xpath = "//div[@class='oxd-input-group__label-wrapper']/following-sibling::div//input"
    assert_css  = ".orangehrm-card-container>h6"

    def pay_functions(self):

        """ Perform actions to navigate to the Pay Grade section."""

        #admin = self.find(By.CSS_SELECTOR,self.admin_css)
        self.click(By.CSS_SELECTOR,self.admin_css)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"):
                #job = self.find(By.XPATH,self.job_xpath)
                self.click(By.XPATH,self.job_xpath)
                #pay = self.find(By.XPATH,self.pay_grade_xpath)
                self.click(By.XPATH,self.pay_grade_xpath)
        
    def paygrade(self,paygrade):

        """Sends the pay grade name in the corresponding text box."""
        
        #name_textbox = self.find(By.XPATH,self.name_textbox_xpath)
        self.send_key(By.XPATH,self.name_textbox_xpath,paygrade)

    def assert_pay(self):

        """Assert that the Pay Grade section is accessed successfully."""
        
        try:
            expected = "Add Pay Grade"
            actual = self.find(By.CSS_SELECTOR,self.assert_css).text
            assert actual.__eq__(expected), f"Assertion failed: expected text is '{expected}', but the actual text is '{actual}'"
            return True
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
            
    