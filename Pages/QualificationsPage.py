"""Author: Keerthesan (Expleo)"""
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class QualificationPage(BasePage):

    def __init__(self, driver):
       super().__init__(driver)

    my_info_css = "a[href='/web/index.php/pim/viewMyDetails']"
    qualifications_css = "a[href='/web/index.php/pim/viewQualifications/empNumber/7']"
    company_name_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    job_title_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    from_date_xpath = "(//input[@placeholder='yyyy-dd-mm'])[1]"
    to_date_xpath = "(//input[@placeholder='yyyy-dd-mm'])[2]"
    comment_xpath = "//div[@data-v-957b4417]//textarea"
    add_but_xpath = "(//button[@type='button'][@class='oxd-button oxd-button--medium oxd-button--text'])[1]"
    assert_xpath = "(//div[@class='oxd-toast-start']//p)[2]"

    def qualification(self):

        """Navigate to the Qualifications page."""
        
        self.click(By.CSS_SELECTOR,self.my_info_css)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"):
                quali = self.find(By.CSS_SELECTOR,self.qualifications_css)
                quali.click()

    def click_add(self):

        """Clicks the 'Add' button."""

        self.click(By.XPATH,self.add_but_xpath)

    def company_name(self,name):

        """Enter the company name in the corresponding text box."""

        self.send_key(By.XPATH,self.company_name_xpath,name)

    def job_title(self,title):

        """Enter the job title in the corresponding text box."""
        
        self.send_key(By.XPATH,self.job_title_xpath,title)

    def from_date(self,date):
        
        """Enter the start date in the corresponding text box."""
    
        self.send_key(By.XPATH,self.from_date_xpath,date)

    def to_date(self,date):

        """Enter the end date in the corresponding text box."""
        
        self.send_key(By.XPATH,self.to_date_xpath,date)

    def comment(self,comment):
    
        """Enter a comment in the corresponding text box."""

        self.send_key(By.XPATH,self.comment_xpath,comment)

    def assert_myinfo(self):

        """Assert the success message after saving."""
        
        try:
            expected = "Successfully Saved"
            actual = self.find(By.XPATH,self.assert_xpath).text
            assert actual.__eq__(expected), f"Assertion failed: expected text is '{expected}', but the actual text is '{actual}'"
            return True
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False