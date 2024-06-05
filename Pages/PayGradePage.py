import time
from selenium.webdriver.common.by import By
from Pages.JobPage import JobPage
from selenium.webdriver.support import expected_conditions as ec


class PayGradePage(JobPage):

    def __init__(self, driver):
       super().__init__(driver)

    job_xpath = "(//div[@class='oxd-topbar-body']//span)[2]"
    pay_grade_xpath = "(//ul[@class='oxd-dropdown-menu']//li)[2]"
    name_textbox_xpath = "//div[@class='oxd-input-group__label-wrapper']/following-sibling::div//input"
    assert_css  = ".orangehrm-card-container>h6"

    def pay_functions(self):
        admin = self.find(By.CSS_SELECTOR,self.admin_css)
        self.click(admin)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"):
                job = self.find(By.XPATH,self.job_xpath)
                self.click(job)
                pay = self.find(By.XPATH,self.pay_grade_xpath)
                self.click(pay)
        
    def paygrade(self,paygrade):
        name_textbox = self.find(By.XPATH,self.name_textbox_xpath)
        self.send_key(name_textbox,paygrade)

    def assert_pay(self):
        expected = "Add Pay Grade"
        actual = self.find(By.CSS_SELECTOR,self.assert_css).text
        return actual.__eq__(expected)
    