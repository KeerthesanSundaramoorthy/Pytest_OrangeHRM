import time
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
        admin = self.find(By.CSS_SELECTOR,self.admin_css)
        self.click(admin)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"):
                job = self.find(By.XPATH,self.job_xpath)
                self.click(job)
                job_titles = self.find(By.XPATH,self.job_titles_xpath)
                self.click(job_titles)
    

    def job_title(self,title):
        job_title_field = self.find(By.XPATH,self.job_text_xpath)
        self.send_key(job_title_field,title)

    def job_description(self,desc):
        job_desc_field = self.find(By.XPATH,self.job_desc_xpath)
        self.send_key(job_desc_field,desc)

    def job_note(self,note):
        job_note_field = self.find(By.XPATH,self.jb_note_xpath)
        self.send_key(job_note_field,note)
    
    def click_cancel(self):
        cancel_but = self.find(By.XPATH,self.cancel_button_xpath)
        self.click(cancel_but)

    def job_delete(self):
        delete = self.find(By.XPATH,self.trash_xpath)
        self.click(delete)
        yes = self.find(By.XPATH,self.yes_del_xpath)
        self.click(yes)

    def assert_job(self):
        expected = "Successfully Saved"
        actual = self.find(By.XPATH,self.success_saved_xpath).text
        return actual.__eq__(expected)
    
    def assert_previous(self):
        return self.find(By.XPATH,self.trash_xpath).is_displayed()
    
    def assert_delete(self):
        return self.find(By.XPATH,self.success_deleted_xpath).is_displayed()

