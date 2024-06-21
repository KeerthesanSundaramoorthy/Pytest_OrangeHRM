"""Author: Suvetha (Expleo)"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Personal_details import PersonalDetailsPage
from Utility import Excel_Reader, console_logger

@pytest.mark.usefixtures("setup_and_teardown")
class TestPersonalDetails:

    """TestPersonalDetails class contains test methods to add personal details."""

    log = console_logger.get_logger()

    @pytest.mark.smoke
    @pytest.mark.parametrize("Fname,Mname,Lname,Employee_id,Othr_id,Lnumber,Exp_date,dob", Excel_Reader.get_data("E:\gitpytest_clone\Pytest_OrangeHRM\Excel_Files\PersonalDetailsData.xlsx", "PersonalDetails"))
    def test_personal_details(self, Fname, Mname, Lname, Employee_id, Othr_id, Lnumber, Exp_date, dob):

        """This test case checks the workflow of logging into the application, clicking the personal details,
        and verifying that the required details are uploaded successfully."""

        personal_details_page = PersonalDetailsPage(self.driver)
        personal_details_page.valid_login()
        self.log.info("Logged in successfully")
        personal_details_page.personalDetails(Fname, Mname, Lname, Employee_id, Othr_id, Lnumber, Exp_date, dob)
        personal_details_page.select_gender("female")
        self.log.info("Gender 'female' selected")
        personal_details_page.select_country("Indian")
        self.log.info("Country 'Indian' selected")
        personal_details_page.select_status("Single")
        self.log.info("Status 'Single' selected")
        personal_details_page.save_details()
        self.log.info("Personal details saved")
        personal_details_page.assert_details_saved_successfully()
        self.log.info("Personal details verified successfully")

    @pytest.mark.smoke
    @pytest.mark.parametrize("Fname,Mname,Lname", [("Monik", "Jayagopi", "J"),])
    def test_personal_details_mandatory(self, Fname, Mname, Lname):

        """This test case checks the workflow of logging into the application, clicking the personal details,
        and verifying that the required details are uploaded successfully in the mandatory fields."""

        personal_details_page = PersonalDetailsPage(self.driver)
        personal_details_page.valid_login()
        self.log.info("Logged in successfully")
        personal_details_page.personalDetails_mandatory(Fname, Mname, Lname)
        personal_details_page.save_details()
        self.log.info("Personal details saved")
        personal_details_page.assert_details_saved_successfully()
        self.log.info("Personal details verified successfully")
