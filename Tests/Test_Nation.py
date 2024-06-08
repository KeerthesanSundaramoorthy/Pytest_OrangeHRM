"""Author: Keerthesan (Expleo)"""
import pytest
from Utility import console_logger
from Pages.NationPage import NationPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestNation:

    """TestNation class contains test methods to validate the new nation for the organization is added on the nation page."""
    
    log = console_logger.get_logger()
    
    @pytest.mark.smoke
    def test_new_nation(self):

        """This test case checks the workflow of logging into the application, navigating to the Nationalities section,
        adding a new nation, and verifying that the nation is successfully saved."""

        name = utility_file.get_config("Nation Details","new_name")
        nation = NationPage(self.driver)
        nation.valid_login()
        self.log.info("Successfully logged into the application")
        nation.nationalities()
        self.log.info("Nationalities is clicked from the drop down successfully")
        nation.add()
        self.log.info("Add button is clicked")
        nation.nation_name(name)
        self.log.info("Nation name is typed in the appropriate text box")
        nation.click_save()
        self.log.info("Save button is clicked") 
        nation.assert_new_nation()
        self.log.info("Successfully Saved message is seen and verified")

    @pytest.mark.regression
    def test_existing_nation(self):

        """This test case checks the workflow of logging into the application, navigating to the Nationalities section,
        attempting to add an existing nation, and verifying that the "Already exists" message is displayed."""

        name = utility_file.get_config("Nation Details","existing_name")
        nation = NationPage(self.driver)
        nation.valid_login()
        self.log.info("Successfully logged into the application")
        nation.nationalities()
        self.log.info("Nationalities is clicked from the drop down successfully")
        nation.add()
        self.log.info("Add button is clicked")
        nation.nation_name(name)
        self.log.info("Nation name is typed in the appropriate text box")
        nation.click_save()
        self.log.info("Save button is clicked") 
        nation.assert_existing_nation()
        self.log.info("Already exists message is seen and verified")

