"""Author: Keerthesan (Expleo)"""
import pytest
from Utility import console_logger
from Pages.UserPage import UserPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestUser:

    """TestUser class contains the methods to validate the search feature of the admin on the user management page."""
    
    log = console_logger.get_logger()
    
    @pytest.mark.smoke
    def test_valid_search(self):
        
        """This test case verifies the workflow of performing a valid search for a user by filling all the fields."""

        user_page = UserPage(self.driver)
        user_page.valid_login()
        self.log.info("Successfully logged into the application")
        user_page.user_management()
        self.log.info("Users is clicked from the drop down successfully")
        username1 = utility_file.get_config("valid user details","username1")
        emp_name = utility_file.get_config("valid user details","emp_name")
        user_page.username(username1) 
        self.log.info("Username is typed in the username text box")
        user_page.ess_userrole()
        self.log.info("ess is selected as the user role")
        user_page.employee_name(emp_name)
        self.log.info("Employee name is typed in the Employee name text box")
        user_page.select_status()
        self.log.info("Enable status is selected")
        user_page.search()
        self.log.info("Search Button is clicked")
        assert user_page.search_assert()
        self.log.info("Search result is verified successfully")

    @pytest.mark.smoke
    def test_partial_search(self):

        """This test case verifies the workflow of performing a valid search for a user by filling the required fields."""
        
        user_page = UserPage(self.driver)
        user_page.valid_login()
        self.log.info("Successfully logged into the application")
        user_page.user_management()
        self.log.info("Users is clicked from the drop down successfully")
        username1 = utility_file.get_config("partial user details","username1")
        user_page.username(username1) 
        self.log.info("Username is typed in the username text box")
        user_page.select_status()
        self.log.info("Enable status is selected")
        user_page.search()
        self.log.info("Search Button is clicked")
        assert user_page.search_assert()
        self.log.info("Search result is verified successfully")

    @pytest.mark.regression
    def test_invalid_search(self):

        """This test case verifies the workflow of performing an invalid search for a user."""

        user_page = UserPage(self.driver)
        user_page.valid_login()
        self.log.info("Successfully logged into the application")
        user_page.user_management()
        self.log.info("Users is clicked from the drop down successfully")
        username1 = utility_file.get_config("invalid user details","username1")
        user_page.username(username1) 
        self.log.info("Username is typed in the username text box") 
        user_page.admin_userrole()
        self.log.info("Admin is selected as the user role")
        user_page.search()
        self.log.info("Search Button is clicked")
        assert user_page.search_assert()
        self.log.info("Search result is verified successfully")