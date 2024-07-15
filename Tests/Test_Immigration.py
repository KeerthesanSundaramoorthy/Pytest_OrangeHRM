"""Author: Suvetha (Expleo)"""
import pytest
from Pages.Immigration import ImmigrationPage
from Utility import Excel_Reader, console_logger

@pytest.mark.usefixtures("setup_and_teardown")
class TestImmigration:
    """TestImmigration class contains test methods to add immigration details."""

    log = console_logger.get_logger()

    @pytest.mark.smoke
    @pytest.mark.parametrize("number, issued_date, expiry_date, status, review_date, comment", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\Excel_Files\\ImmigrationData.xlsx", "immigration"))
    def test_add_immigration_details(self, number, issued_date, expiry_date, status, review_date, comment):
        """This test case checks the workflow of logging into the application, clicking the immigration,
        and verifying that the required details is uploaded successfully."""

        immigration_page = ImmigrationPage(self.driver)
        immigration_page.valid_login()
        self.log.info("Logged in successfully")
        immigration_page.add_immigration_details(number, issued_date, expiry_date, status, review_date, comment)
        immigration_page.select_country("Algeria")
        self.log.info("Country 'Algeria' selected")
        immigration_page.save_details()
        self.log.info("Immigration details saved")
        immigration_page.assert_details_saved_successfully()
        self.log.info("Immigration details verified successfully")

    @pytest.mark.regression
    @pytest.mark.parametrize("number, issued_date, expiry_date, status, review_date, comment", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\Excel_Files\\ImmigrationData.xlsx", "immigration"))
    def test_add_immigration_details_cancel(self, number, issued_date, expiry_date, status, review_date, comment):
        """This test case checks the workflow of logging into the application, clicking the immigration,
        and verifying that the cancel was done."""

        immigration_page = ImmigrationPage(self.driver)
        immigration_page.valid_login()
        self.log.info("Logged in successfully")
        immigration_page.add_immigration_details(number, issued_date, expiry_date, status, review_date, comment)
        immigration_page.select_country("Algeria")
        self.log.info("Country 'Algeria' selected")
        immigration_page.cancel_details()
        self.log.info("Immigration details entry canceled")
