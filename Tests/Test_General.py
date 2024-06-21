"""Author: Keerthesan (Expleo)"""
import pytest
from Utility import console_logger
from Pages.GenInfoPage import GeneralPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestGeneral:

    """ TestGeneral class contains test methods to perform and validate various actions on the general information page."""

    log = console_logger.get_logger()
    
    @pytest.mark.smoke
    def test_edit(self):
        
        """ This test case checks the workflow of logging into the application, accessing the general information section,
        and verifying that all text boxes are editable."""

        gen = GeneralPage(self.driver)
        gen.valid_login()
        self.log.info("Successfully logged into the application")
        gen.general_function()
        self.log.info("General Information is clicked from the drop down successfully")
        assert gen.assert_editable()
        self.log.info("All the text box is enabled and verified")

    @pytest.mark.regression
    def test_edit_name(self):

        """This test case checks the workflow of logging into the application, updating the organization name,
        and verifying that the change is successfully saved."""

        name = utility_file.get_config("Organization name","name")
        gen = GeneralPage(self.driver)
        gen.valid_login()
        self.log.info("Successfully logged into the application")
        gen.general_function()
        self.log.info("General Information is clicked from the drop down successfully")
        gen.enter_name(name)
        self.log.info("Organization Name is typed in the appropriate text box")
        gen.save_but()
        self.log.info("Save button is clicked") 
        assert gen.assert_added()
        self.log.info("Successfully Updated message is seen and verified")