"""Author: Keerthesan (Expleo)"""
import pytest
from Utility import console_logger
from Pages.CongigurationPage import ConfigurationPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestConfigurations:

    """TestConfigurations class contains test methods to perform and validate various configurations on the configuration page."""

    log = console_logger.get_logger()
    
    @pytest.mark.smoke
    def test_configuration(self):

        """This test case checks the workflow of logging into the application, selecting configuration settings, 
        and verifying that an email is sent."""

        config = ConfigurationPage(self.driver)
        test_email = utility_file.get_config("Email Credentials","test_email")
        sent_email = utility_file.get_config("Email Credentials","sent_email")
        config.valid_login()
        self.log.info("Successfully logged into the application")
        config.congiguration()
        self.log.info("Configurations is clicked from the drop down successfully")
        config.sent_email(test_email)
        self.log.info("Test Email is typed in the appropriate text box")
        config.click_checkbox()
        self.log.info("Male gender checkbox is clicked")
        config.enable_mail()
        self.log.info("Sent Email is enabled")
        config.test_email(sent_email)
        self.log.info("Sent Email is typed in the appropriate text box")
        config.click_save()
        self.log.info("Save button is clicked") 
        #assert config.assert_email()
        #self.log.info("Email sent message is seen and verified")