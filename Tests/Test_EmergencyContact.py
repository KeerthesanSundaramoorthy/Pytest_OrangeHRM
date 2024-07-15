"""Author: Suvetha (Expleo)"""
import pytest
from Pages.EmergencyContact import EmergencyContactPage
from Utility import Excel_Reader, console_logger

@pytest.mark.usefixtures("setup_and_teardown")
class TestEmergencyContact:
    """TestEmergencyContact class contains test methods to add emergency contact details."""

    log = console_logger.get_logger()

    @pytest.mark.smoke
    @pytest.mark.parametrize("name,relationship,telephone,mobile,work", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\Excel_Files\\EmergencyContactData.xlsx", "emergency"))
    def test_add_emergency_contact(self, name, relationship, telephone, mobile, work):
        """This test case checks the workflow of logging into the application, clicking the emergency contact,
        and verifying that the mandatory details is uploaded successfully."""

        emergency_contact_page = EmergencyContactPage(self.driver)
        emergency_contact_page.valid_login()
        self.log.info("Logged in successfully")
        emergency_contact_page.emergencyContact(name, relationship, telephone, mobile, work)
        emergency_contact_page.save_details()
        self.log.info("Emergency contact details saved")
        emergency_contact_page.assert_update_message_displayed()
        self.log.info("Emergency contact details verified successfully")

    @pytest.mark.regression
    @pytest.mark.parametrize("name,relationship,telephone,mobile,work", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\Excel_Files\\EmergencyContactData.xlsx", "emergency"))
    def test_add_emergency_contact_cancel(self, name, relationship, telephone, mobile, work):
        """This test case checks the workflow of logging into the application, clicking the emergency contact,
        and verifying that the cancel is done."""

        emergency_contact_page = EmergencyContactPage(self.driver)
        emergency_contact_page.valid_login()
        self.log.info("Logged in successfully")
        emergency_contact_page.emergencyContact(name, relationship, telephone, mobile, work)
        emergency_contact_page.cancel_details()
        self.log.info("Emergency contact details entry canceled")

    @pytest.mark.smoke
    @pytest.mark.parametrize("name,relationship,telephone,mobile,work", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\Excel_Files\\EmergencyContactData.xlsx", "mandatory"))
    def test_add_emergency_contact_mandatory(self, name, relationship, telephone, mobile, work):
        """This test case checks the workflow of logging into the application, clicking the emergency contact,
        and verifying that the mandatory details is uploaded successfully."""

        emergency_contact_page = EmergencyContactPage(self.driver)
        emergency_contact_page.valid_login()
        self.log.info("Logged in successfully")
        emergency_contact_page.emergencyContact_mandatory(name, relationship, telephone)
        emergency_contact_page.save_details()
        self.log.info("Mandatory emergency contact details saved")
        emergency_contact_page.assert_update_message_displayed()
        self.log.info("Mandatory emergency contact details verified successfully")

    @pytest.mark.smoke
    @pytest.mark.parametrize("name,relationship,telephone,mobile,work", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\Excel_Files\\EmergencyContactData.xlsx", "required"))
    def test_add_emergency_contact_required(self, name, relationship, telephone, mobile, work):
        """This test case checks the workflow of logging into the application, clicking the emergency contact,
        and verifying that the required details is uploaded successfully."""

        emergency_contact_page = EmergencyContactPage(self.driver)
        emergency_contact_page.valid_login()
        self.log.info("Logged in successfully")
        emergency_contact_page.emergencyContact_required(name, relationship)
        emergency_contact_page.save_details()
        self.log.info("Required emergency contact details saved")
        emergency_contact_page.assert_error_message_displayed()
        self.log.info("Required emergency contact details error message verified successfully")
