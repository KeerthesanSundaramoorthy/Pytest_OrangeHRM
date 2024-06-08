"""Author: Keerthesan (Expleo)"""
import pytest
from Utility import console_logger
from Pages.LocationPage import LocationPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestLocation:

    """TestLocation class contains test methods to validate the new location for the organization is added on the location page."""
    
    log = console_logger.get_logger()
    
    @pytest.mark.smoke
    def test_location(self):

        """This test case checks the workflow of logging into the application, 
        selecting Location from the dropdown, filling in the location form with 
        name and city, clicking the search button, and verifying the search result."""

        name = utility_file.get_config("Location Details","name")
        city = utility_file.get_config("Location Details","city")
        location = LocationPage(self.driver)
        location.valid_login()
        self.log.info("Successfully logged into the application")
        location.locations()
        self.log.info("Location is clicked from the drop down successfully")
        location.form_fill(name,city)
        self.log.info("Location is filled and name,city is is typed in the appropriate text box")
        location.click_search()
        self.log.info("Search button is clicked") 
        assert location.assert_result()
        self.log.info("Search result is seen and verified successfully")