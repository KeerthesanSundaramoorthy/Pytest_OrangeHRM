"""Author: Keerthesan (Expleo)"""
from selenium.webdriver.common.by import By
from Pages.JobPage import JobPage

class GeneralPage(JobPage):

    def __init__(self, driver):
       super().__init__(driver)

    organization_xpath = "(//i[@class='oxd-icon bi-chevron-down']/ancestor::span)[3]"
    gen_Info_xpath = "(//ul[@class='oxd-dropdown-menu']//a)[1]"
    edit_xpath = "//input[@type='checkbox']/following-sibling::span"
    org_name_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    save_but_xpath = "(//p[@class='oxd-text oxd-text--p orangehrm-form-hint']//following-sibling::button)"
    assert_xpath = "(//div[@class='oxd-toast-start']//p)[2]"

    def general_function(self):

        """Performs a click on the general function on the General Page."""
        
        self.click(By.CSS_SELECTOR,self.admin_css)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"):
                self.click(By.XPATH,self.organization_xpath)
                self.click(By.XPATH,self.gen_Info_xpath)
                self.click(By.XPATH,self.edit_xpath)

    def assert_editable(self):

        """Check if the organization name field is editable."""
        
        return self.find(By.XPATH,self.org_name_xpath).is_enabled()

    def enter_name(self,name):

        """Enter a new organization name."""

        org = self.find(By.XPATH,self.org_name_xpath).clear()
        self.send_key(By.XPATH,self.org_name_xpath,name)

    def save_but(self):

        """Clicks the save button."""
        
        self.click(By.XPATH,self.save_but_xpath)

    def assert_added(self):

        """ Assert if the organization name has been successfully updated."""
        
        try:
            expected = "Successfully Updated"
            actual = self.find(By.XPATH,self.assert_xpath).text
            assert actual.__eq__(expected), f"Assertion failed: expected text is '{expected}', but the actual text is '{actual}'"
            return True
                
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

