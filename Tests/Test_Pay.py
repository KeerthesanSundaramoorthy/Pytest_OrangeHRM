"""Author: Keerthesan (Expleo)"""
import pytest
from Utility import console_logger
from Pages.PayGradePage import PayGradePage
from Utility import Excel_Reader

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("paygrade",Excel_Reader.get_data("E:\\Pytest_OrangeHRM\\Excel_Files\\Pay_Grade.xlsx","Sheet1"))
class TestPay:

    """TestPay class contains test methods to verify the new pay grade is added on the pay grade page."""
    
    log = console_logger.get_logger()
    
    @pytest.mark.smoke
    def test_add_paygrade(self,paygrade):

        """ This test case checks the workflow of logging into the application, navigating to the pay grade section,
        adding a new pay grade, and verifying that the pay grade is saved successfully."""

        pay = PayGradePage(self.driver)
        pay.valid_login()
        self.log.info("Successfully logged into the application")
        pay.pay_functions()
        self.log.info("Pay Grade is clicked from the drop down successfully")
        pay.add()
        self.log.info("Add button is clicked")
        pay.paygrade(paygrade[0])
        self.log.info("Pay Grade is typed in the appropriate text box") 
        pay.click_save()
        self.log.info("Save button is clicked") 
        pay.assert_pay()
        self.log.info("Successfully Saved message is seen and verified")
