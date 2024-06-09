from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class Dashboard_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # QuickLaunch Icon locators
    assign_leave_xpath = "(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[1]"
    leave_list_xpath =  "(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[2]"
    timeSheet_page_xpath = "(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[3]"
    apply_leave_xpath = "(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[4]"
    my_leave_xpath = "(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[5]"
    my_timesheet_xpath = "(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[6]"

 # Assert locators
    leave_assert = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"
    timesheet_assert = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"

    #Employee Leave List
    list_xpath = "(//div[@class='orangehrm-dashboard-widget-body'])[3]"
    def assign_leave(self):
        self.find(By.XPATH,self.assign_leave_xpath).click()
        
    def leave_list(self):
        self.find(By.XPATH,self.leave_list_xpath).click()

    def timesheet_page(self):
        self.find(By.XPATH,self.timeSheet_page_xpath).click()

    def apply_leave(self):
        self.find(By.XPATH,self.apply_leave_xpath).click()

    def my_leave(self):
        self.find(By.XPATH,self.my_leave_xpath).click()

    def my_timesheet(self):
        self.find(By.XPATH,self.my_timesheet_xpath).click()

    def leave_page_navigate(self):
        leave_element = self.find(By.XPATH,self.leave_assert)
        assert leave_element.is_displayed(),"Leave"

    def timesheet_page_navigate(self):
        timesheet_element = self.find(By.XPATH,self.timesheet_assert)
        assert timesheet_element.is_displayed,"Time"

    #Employee Leave List
    def emp_leavelist(self):
        return self.find(By.XPATH,self.list_xpath)
        