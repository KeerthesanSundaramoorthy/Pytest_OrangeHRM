"""Author: Keerthesan (Expleo)"""
from selenium.webdriver.common.by import By
from Pages.GenInfoPage import GeneralPage
from selenium.webdriver.support import expected_conditions as ec


class LocationPage(GeneralPage):

    def __init__(self, driver):
       super().__init__(driver)

    location_xpath = "(//ul[@class='oxd-dropdown-menu']//a)[2]"
    loc_name_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    city_loc_xpath = "(//div[@data-v-957b4417]//input)[2]"
    country_loc_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1]"
    country_xpath = "//span[text()='United States']"
    verify_xpath = "//span[text()='(1) Record Found']"
    search_button_xpath = "//button[text()=' Search ']"

    def locations(self):

        """Navigate to the location page within the admin section of the application."""

        self.click(By.CSS_SELECTOR,self.admin_css)
        total = self.driver.window_handles
        for i in total:
            self.driver.switch_to.window(i)
            if self.driver.current_url.__eq__("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"):
                self.click(By.XPATH,self.organization_xpath)
                self.click(By.XPATH,self.location_xpath)

    def form_fill(self,name,city):

        """Fill out the location form with provided name and city details."""

        self.send_key(By.XPATH,self.loc_name_xpath,name)
        self.send_key(By.XPATH,self.city_loc_xpath,city)
        self.click(By.XPATH,self.country_loc_xpath)
        us = self.wait.until(ec.element_to_be_clickable((By.XPATH,self.country_xpath)))
        us.click()

    def click_search(self):

        """Click on the search button to initiate the location search."""

        self.click(By.XPATH,self.search_button_xpath)

    def assert_result(self):

        """Assert if the search result is displayed."""
        
        try:
            return self.find(By.XPATH,self.verify_xpath).is_displayed()
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
