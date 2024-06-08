"""Author: Keerthesan (Expleo)"""
from selenium.webdriver.common.by import By
from Pages.JobPage import JobPage


class ConfigurationPage(JobPage):

    def __init__(self, driver):
       super().__init__(driver)

    configurations_xpath = "(//span[@class='oxd-topbar-body-nav-tab-item'])[5]"
    email_config_xpath = "(//ul[@class='oxd-dropdown-menu']//a)[1]"
    checkbox_xpath = "(//div[@class='oxd-radio-wrapper']//span)[3]"
    enable_xpath = "//input[@type='checkbox']/following-sibling::span"
    sent_email_xpath = "(//div[@data-v-957b4417]//input)[1]"
    test_email_xpath = "(//div[@data-v-957b4417]//input)[5]"
    assert_xpath = "(//div[@class='oxd-toast-start']//p)[2]"

    def congiguration(self):

        """Navigate to the configuration page and select email configuration."""

        self.click(By.CSS_SELECTOR,self.admin_css)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"):
                self.click(By.XPATH,self.configurations_xpath)
                self.click(By.XPATH,self.email_config_xpath)

    def sent_email(self,email):

        """Enters the email to be sent."""

        self.send_key(By.XPATH,self.sent_email_xpath,email)

    def click_checkbox(self):
        
        """ Clicks on the Male gender checkbox."""

        self.click(By.XPATH,self.checkbox_xpath)

    def enable_mail(self):

        """ Enables the sent email button."""
        
        self.click(By.XPATH,self.enable_xpath)
        
    def test_email(self,email):

        """Enters the test email address."""
        
        self.send_key(By.XPATH,self.test_email_xpath,email)

    def assert_email(self):
        
        """Asserts whether the test email was sent successfully."""
        
        try:
            expected = "Test Email Sent"
            actual = self.find(By.XPATH,self.assert_xpath).text
            assert actual.__eq__(expected), f"Assertion failed: expected text is '{expected}', but the actual text is '{actual}'"
            return True
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False