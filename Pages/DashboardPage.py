'''from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class Dashboard_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    #QuickLaunck Icon locators
    #assign_leave_xpath = (By.XPATH,"(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[1])")
    assign_leave_xpath = "(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[1])"
    leave_list_xpath =  (By.XPATH,"(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[2])")
    timeSheet_page_xpath = (By.XPATH,"(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[3])")
    apply_leave_xpath = (By.XPATH,"(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[4])")
    my_leave_xpath = (By.XPATH,"(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[5])")
    my_timesheet_xpath = (By.XPATH,"(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[7])")

    #Assert locators

    assign_leave_assert = (By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

    def assign_leave(self):
        #leave = self.find(By.XPATH,self.assign_leave_xpath)
        self.click(By.XPATH,self.assign_leave_xpath)
        assign_element = self.find(*self.assign_leave_assert)
        assign_text = assign_element.text
        assert "Leave" == assign_text
'''



from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class Dashboard_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # QuickLaunch Icon locators
    assign_leave_xpath = "(//button[@class='oxd-icon-button orangehrm-quick-launch-icon']//*[local-name()='svg'])[1]"

    # Assert locators
    assign_leave_assert = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

    def assign_leave(self):
        self.click(By.XPATH, self.assign_leave_xpath)
        assign_element = self.find(*self.assign_leave_assert)
        assign_text = assign_element.text
        assert "Leave" == assign_text
