"""Author: Keerthesan (Expleo)"""
from selenium.webdriver.common.by import By
from Pages.QualificationsPage import QualificationPage
from selenium.webdriver.support import expected_conditions as ec


class Membership(QualificationPage):

    def __init__(self, driver):
       super().__init__(driver)

    membership_css = "a[href='/web/index.php/pim/viewMemberships/empNumber/7']"
    mem_name_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1]"
    acca_xpath = "//span[text()='ACCA']"
    currency_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1]"
    curr_xpath = "//span[text()='Algerian Dinar']"
    amount_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    subscription_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1]"
    subs_xpath = "//span[text()='Company']"
    com_date_xpath = "(//div[@class='oxd-date-input']//input)[1]"
    ren_date_xpath = "(//div[@class='oxd-date-input']//input)[2]"

    def membership(self):

        """Navigate to Membership section."""

        self.click(By.CSS_SELECTOR,self.my_info_css)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"):
                member = self.find(By.CSS_SELECTOR,self.membership_css)
                member.click()

    def select_member(self):

        """Selects the member."""

        self.click(By.XPATH,self.mem_name_xpath)
        acca = self.wait.until(ec.element_to_be_clickable((By.XPATH,self.acca_xpath)))
        acca.click()

    def enter_amount(self,amount):

        """Enters the subscription amount."""

        self.send_key(By.XPATH,self.amount_xpath,amount)

    def select_subscription(self):

        """Selects the subscription type."""

        self.click(By.XPATH,self.subscription_xpath)
        subs = self.wait.until(ec.element_to_be_clickable((By.XPATH,self.subs_xpath)))
        subs.click()

    def select_currency(self):

        """Selects the currency."""

        self.click(By.XPATH,self.currency_xpath)
        curr = self.wait.until(ec.element_to_be_clickable((By.XPATH,self.curr_xpath)))
        curr.click()

    def select_commence_date(self,date):

        """Selects the commencement date."""

        self.send_key(By.XPATH,self.com_date_xpath,date)

    def select_renewal_date(self,date):

        """Selects the renewal date."""

        self.send_key(By.XPATH,self.ren_date_xpath,date)