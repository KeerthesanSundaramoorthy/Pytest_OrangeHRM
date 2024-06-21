"""Author: Keerthesan (Expleo)"""
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as ec


class JobPage(BasePage):

    def __init__(self, driver):
       super().__init__(driver)
    
    admin_css = "a[href='/web/index.php/admin/viewAdminModule']"
    job_xpath = "(//div[@class='oxd-topbar-body']//span)[2]"
    job_titles_xpath = "(//ul[@class='oxd-dropdown-menu']//li)[1]"    
    job_text_xpath = "(//div[@data-v-957b4417]//input)[1]"
    job_desc_xpath = "(//div[@data-v-957b4417]//textarea)[1]"
    jb_note_xpath = "(//div[@class='oxd-input-group oxd-input-field-bottom-space'])[4]//textarea"
    cancel_button_xpath = "(//p[@class='oxd-text oxd-text--p orangehrm-form-hint']//following-sibling::button)[1]"
    trash_xpath = "(//i[@class='oxd-icon bi-trash'])[1]"
    success_deleted_xpath = "//p[text()='Successfully Deleted']"
    yes_del_xpath = "//button[text()=' Yes, Delete ']"
    success_saved_xpath = "(//div[@class='oxd-toast-start']//p)[2]"

    def job_functions(self):

        """Navigates to the job functions page."""
        
        self.click(By.CSS_SELECTOR,self.admin_css)
        #self.click(By.CSS_SELECTOR,self.admin_css)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"):
                self.click(By.XPATH,self.job_xpath)
                self.click(By.XPATH,self.job_titles_xpath)
    

    def job_title(self,title):

        """ Enters the new job title."""
        
        self.send_key(By.XPATH,self.job_text_xpath,title)

    def job_description(self,desc):

        """ Enter the job description."""
        
        self.send_key(By.XPATH,self.job_desc_xpath,desc)

    def job_note(self,note):

        """Enter the job note."""

        self.send_key(By.XPATH,self.jb_note_xpath,note)
    
    def click_cancel(self):

        """Clicks the cancel button."""

        self.click(By.XPATH,self.cancel_button_xpath)

    def job_delete(self):

        """Deletes the job."""

        self.click(By.XPATH,self.trash_xpath)
        self.click(By.XPATH,self.yes_del_xpath)

    def assert_job(self):

        """ Assert job is successfully saved."""
        
        try:
            expected = "Successfully Saved"
            actual = self.find(By.XPATH,self.success_saved_xpath).text
            assert actual.__eq__(expected), f"Assertion failed: expected text is '{expected}', but the actual text is '{actual}'"
            return True
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def assert_previous(self):

        """Assert if the previous page is displayed."""
        
        try:
            return self.find(By.XPATH,self.trash_xpath).is_displayed()
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def assert_delete(self):
        
        """Assert if job is successfully deleted."""
        
        try:
            return self.find(By.XPATH,self.success_deleted_xpath).is_displayed()
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False