"""Author: Keerthesan (Expleo)"""
from selenium.webdriver.common.by import By
from Pages.JobPage import JobPage


class NationPage(JobPage):

    def __init__(self, driver):
       super().__init__(driver)

    nationalities_xpath = "//div[@class='oxd-topbar-body']//a"
    nation_textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    existing_xpath = "//span[text()='Already exists']"
    assert_xpath = "(//div[@class='oxd-toast-start']//p)[2]"

    def nationalities(self):

        """Clicks on the 'Nationalities' link on the page."""

        self.click(By.CSS_SELECTOR,self.admin_css)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"):
                self.click(By.XPATH,self.nationalities_xpath)

    def nation_name(self,name):

        """Enters the name of a nation in the corresponding text box."""

        self.send_key(By.XPATH,self.nation_textbox_xpath,name)

    def assert_new_nation(self):

        """Asserts if a new nation has been successfully saved."""

        try:
            expected = "Successfully Saved"
            actual = self.find(By.XPATH,self.assert_xpath).text
            assert actual.__eq__(expected), f"Assertion failed: expected text is '{expected}', but the actual text is '{actual}'"
            return True
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def assert_existing_nation(self):

        """Asserts if the nation is already added."""

        try:
            expected = "Already exists"
            actual = self.find(By.XPATH,self.existing_xpath).text
            assert actual.__eq__(expected), f"Assertion failed: expected text is '{expected}', but the actual text is '{actual}'"
            return True
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False