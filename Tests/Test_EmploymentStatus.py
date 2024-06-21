"""Author: Keerthesan (Expleo)"""
import pytest
from Utility import console_logger
from Pages.EmploymentPage import EmploymentPage
from Utility import Excel_Reader

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("status",Excel_Reader.get_data("E:\gitpytest_clone\Pytest_OrangeHRM\Excel_Files\Pay_Grade.xlsx","Sheet2"))
class TestEmployment:

    """TestEmployment class contains test methods to validate the adding of new employment status on the employment page."""

    log = console_logger.get_logger()
    
    @pytest.mark.smoke
    def test_add_status(self,status):

        """This test case checks the workflow of logging into the application, clicking the Employment Status option,
        and verifying that the status is added and saved successfully."""
        
        emp = EmploymentPage(self.driver)
        emp.valid_login()
        self.log.info("Successfully logged into the application")
        emp.employ_status()
        self.log.info("Employment Status is clicked from the drop down successfully")
        emp.add()
        self.log.info("Add button is clicked")
        emp.add_employ_status(status[0])
        self.log.info("Employment name is typed in the appropriate text box")
        emp.click_save()
        self.log.info("Save button is clicked") 
        assert emp.assert_employ()
        self.log.info("Successfully Saved message is seen and verified")
