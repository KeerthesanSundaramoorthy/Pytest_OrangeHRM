"""Author: Keerthesan (Expleo)"""
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException, JavascriptException


class DashboardPage(BasePage):
    
    def __init__(self, driver):
       super().__init__(driver)

    clock_css = "button[class='oxd-icon-button oxd-icon-button--solid-main orangehrm-attendance-card-action'][type='button']"
    punch_out_xpath = "(//div[@class='orangehrm-paper-container']//label)[1]"
    pending_xpath = "(//div[@class='orangehrm-todo-list']//p)[1]"
    review_xpath = "(//div[@class='orangehrm-todo-list']//p)[2]"
    my_review_xpath = "//h6[contains(@class,'oxd-text oxd-text--h6 orangehrm-main-title')]"
    candidates_xpath = "//h5[text()='Candidates']"

    def click_clock(self):

        """Clicks on the clock button."""

        try:
            self.click(By.CSS_SELECTOR,self.clock_css)
        
        except TimeoutException as e:
            print(f"TimeoutException: Element {self.clock_css} not clickable after waiting. {e}")
        
        except NoSuchElementException as e:
            print(f"NoSuchElementException: Element {self.clock_css} not found. {e}")
        
        except Exception as e:
            print(f"Exception occurred while trying to click element {self.clock_css}. {e}")
    
    def assert_punch(self):

        """Asserts the punch-out text."""

        try:
            actual = "Date"
            expected = self.find(By.XPATH, self.punch_out_xpath).text
            assert actual.__eq__(expected), f"Assertion failed: expected text is '{expected}', but the actual text is '{actual}'"
            return True
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def pending_review(self):

        """Clicks on the pending review element."""

        try:
            self.click(By.XPATH,self.pending_xpath)
        
        except TimeoutException as e:
            print(f"TimeoutException: Element {self.pending_xpath} not clickable after waiting. {e}")
        
        except NoSuchElementException as e:
            print(f"NoSuchElementException: Element {self.pending_xpath} not found. {e}")
        
        except Exception as e:
            print(f"Exception occurred while trying to click element {self.pending_xpath}. {e}")
    
    def assert_performance(self):

        """Asserts the performance review text."""

        try:
            actual = "My Reviews"
            expected = self.find(By.XPATH,self.my_review_xpath).text
            assert actual.__eq__(expected), f"Assertion failed: expected text is '{expected}', but the actual text is '{actual}'"
            return True
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def remaining_review(self):

        """Clicks on the remaining review element."""

        try:
            self.click(By.XPATH,self.review_xpath)
        
        except TimeoutException as e:
            print(f"TimeoutException: Element {self.review_xpath} not clickable after waiting. {e}")
        
        except NoSuchElementException as e:
            print(f"NoSuchElementException: Element {self.review_xpath} not found. {e}")
        
        except Exception as e:
            print(f"Exception occurred while trying to click element {self.review_xpath}. {e}")

    def assert_recruitment(self):

        """ Asserts the recruitment text."""

        try:
            actual = "Candidates"
            expected = self.find(By.XPATH,self.candidates_xpath).text
            assert actual.__eq__(expected), f"Assertion failed: expected text is '{expected}', but the actual text is '{actual}'"
            return True
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
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
        
