"""Author: Keerthesan (Expleo)"""
import pytest
from Utility import console_logger
from Pages.MembershipPage import Membership
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestMembership:

    """TestMembership class contains test methods to validate the new membership is added on the membership page."""
    
    log = console_logger.get_logger()
    
    @pytest.mark.smoke
    def test_member(self):

        """ This test case checks the workflow of logging into the application, navigating to the Membership section,
        adding a new member with all required details, and verifying that the 'Successfully Saved' message is seen."""

        amount = utility_file.get_config("Membership Details","amount")
        com_date = utility_file.get_config("Membership Details","com_date")
        ren_date = utility_file.get_config("Membership Details","ren_date")
        member = Membership(self.driver)
        member.valid_login()
        self.log.info("Successfully logged into the application")
        member.membership()
        self.log.info("Membership is clicked from the list successfully")
        member.click_add()
        self.log.info("Add button is clicked")
        member.select_member()
        self.log.info("Acca is selected as the member role")
        member.select_subscription()
        self.log.info("Company is selected as the subscription method")
        member.enter_amount(amount)
        self.log.info("Subscription amount is typed in the appropriate text box")
        member.select_currency()
        self.log.info("Appropriate currency is selected")
        member.select_commence_date(com_date)
        self.log.info("Commence date is typed in the appropriate text box")
        member.select_renewal_date(ren_date)
        self.log.info("Renewal date is typed in the appropriate text box")
        member.click_save()
        self.log.info("Save button is clicked") 
        assert member.assert_myinfo()
        self.log.info("Successfully Saved message is seen and verified")

    @pytest.mark.regression
    def test_man_member(self):

        """This test case checks the workflow of logging into the application, navigating to the Membership section,
        adding a new member with mandatory details, and verifying that the 'Successfully Saved' message is seen."""

        member = Membership(self.driver)
        member.valid_login()
        self.log.info("Successfully logged into the application")
        member.membership()
        self.log.info("Membership is clicked from the list successfully")
        member.click_add()
        self.log.info("Add button is clicked")
        member.select_member()
        self.log.info("Acca is selected as the member role")
        member.click_save()
        self.log.info("Save button is clicked") 
        assert member.assert_myinfo()
        self.log.info("Successfully Saved message is seen and verified")