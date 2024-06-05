import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as ec


class UserPage(BasePage):

    def __init__(self, driver):
       super().__init__(driver)

    admin_css = "a[href='/web/index.php/admin/viewAdminModule']"
    user_man_xpath = "(//div[@class='oxd-topbar-body']//span)[1]"
    users_xpath = "//ul[@class='oxd-dropdown-menu']//a"
    username_xpath = "(//div[@class='oxd-grid-item oxd-grid-item--gutters']//input)[1]"
    user_role_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1]"
    ess_xpath = "//span[text()='ESS']"
    employee_name_xpath = "//input[@placeholder='Type for hints...']"
    status_xpath = "(//div[@class='oxd-select-text oxd-select-text--active']//div)[3]"
    enabled_xpath = "//span[text()='Enabled']"
    search_button_xpath = "//button[text()=' Search ']"
    admin_role_xpath = "//span[text()='Admin']"
    assert_user_xpath = "(//div[@class='oxd-table-header']//div)[4]"

    def user_management(self):
        admin = self.find(By.CSS_SELECTOR,self.admin_css)
        self.click(admin)
        #self.driver.open_new_window_action()
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"):
                user_man = self.find(By.XPATH,self.user_man_xpath)
                self.click(user_man)
                users = self.find(By.XPATH,self.users_xpath)
                self.click(users)

    def username(self,user):
        username_field = self.find(By.XPATH,self.username_xpath)
        self.send_key(username_field,user)

    def ess_userrole(self):
        user_role = self.find(By.XPATH,self.user_role_xpath)
        self.click(user_role)
        ess = self.wait.until(ec.element_to_be_clickable((By.XPATH,self.ess_xpath)))
        self.click(ess)
        time.sleep(2)

    def admin_userrole(self):
        user_role1 = self.find(By.XPATH,self.user_role_xpath)
        self.click(user_role1)
        admin = self.wait.until(ec.element_to_be_clickable((By.XPATH,self.admin_role_xpath)))
        self.click(admin)
        time.sleep(2)

    def employee_name(self,emp_name):
        empl_name = self.find(By.XPATH,self.employee_name_xpath)
        self.send_key(empl_name,emp_name)
        emp = self.wait.until(ec.element_to_be_clickable((By.XPATH,"//span[text()='James  Butler']")))
        self.click(emp)

    def select_status(self):
        status = self.find(By.XPATH,self.status_xpath)
        self.click(status)
        enabled = self.wait.until(ec.element_to_be_clickable((By.XPATH,self.enabled_xpath)))
        self.click(enabled)

    def search(self):
        search = self.find(By.XPATH,self.search_button_xpath)
        self.click(search)

    def search_assert(self):
        return self.find(By.XPATH,self.assert_user_xpath).is_displayed()
        '''actual =  self.find(By.XPATH,self.assert_user_xpath).text()
        expected = "Username"
        if actual.__eq__(expected):
            return True
        else:
            return False'''