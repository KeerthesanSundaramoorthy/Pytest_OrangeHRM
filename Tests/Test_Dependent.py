"""Author: Suvetha (Expleo)"""
import pytest
from Pages.Dependent import DependentPage
from Utility import Excel_Reader, console_logger

@pytest.mark.usefixtures("setup_and_teardown")
class TestDependent:
    """TestDependent class contains test methods to add dependent details."""

    log = console_logger.get_logger()

    @pytest.mark.smoke
    @pytest.mark.parametrize("name,dob", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\Excel_Files\\DependentData.xlsx", "dependent"))
    def test_add_dependent(self, name, dob):  
        """This test case checks the workflow of logging into the application, clicking the dependent,
        and verifying that the details is uploaded successfully."""
        
        dependent_page = DependentPage(self.driver)
        dependent_page.valid_login()
        self.log.info("Logged in successfully")
        dependent_page.dependent(name, dob)
        dependent_page.select_relationship("Child")
        dependent_page.save_details()
        self.log.info("Dependent details saved")
        dependent_page.assert_details_saved_successfully()
        self.log.info("Dependent details verified successfully")

    @pytest.mark.regression
    @pytest.mark.parametrize("name,dob", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\Excel_Files\\DependentData.xlsx", "dependent"))
    def test_add_dependent_cancel(self, name, dob):  
        """This test case checks the workflow of logging into the application, clicking the dependent,
        and verifying that the cancel is done."""
        
        dependent_page = DependentPage(self.driver)
        dependent_page.valid_login()
        self.log.info("Logged in successfully")
        dependent_page.dependent(name, dob)
        dependent_page.select_relationship("Child")
        dependent_page.cancel_details()
        self.log.info("Dependent details entry canceled")

    @pytest.mark.parametrize("name", ["Suvetha"])
    def test_add_dependent_mandatory(self, name): 
        """This test case checks the workflow of logging into the application, clicking the dependent,
        and verifying that the mandatory details is uploaded successfully."""

        dependent_page = DependentPage(self.driver)
        dependent_page.valid_login()
        self.log.info("Logged in successfully")
        dependent_page.dependent_mandatory(name)
        dependent_page.select_relationship("Child")
        dependent_page.save_details()
        self.log.info("Dependent mandatory details saved")
        dependent_page.assert_details_saved_successfully()
        self.log.info("Dependent mandatory details verified successfully")
