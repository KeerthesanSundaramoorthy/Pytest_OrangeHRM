"""Author: Suvetha (Expleo)"""
import pytest
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Pages.ChangePasswordPage import ChangePasswordPage
from Utility import utility_file, console_logger

current_password = "admin123"
invalidCurrentPassword = "Admin"
new_password = "User123"
invalidConfirmPassword = "user"
confirm_password = "User123"

@pytest.mark.usefixtures("setup_and_teardown")
class TestChangePassword:
    """TestChangePassword class contains test methods to change password."""
    
    log = console_logger.get_logger()

    @pytest.mark.smoke
    def test_change_password(self):
        """This test case checks the workflow of logging into the application, clicking the change password,
        and verifying that the password is changed."""


        changepassword = ChangePasswordPage(self.driver)
        changepassword.valid_login()
        self.log.info("Logged in successfully")
        changepassword.changePassword(current_password, new_password, confirm_password)
        changepassword.assert_password_change_successful()
        self.log.info("Password change verified successfully")

    @pytest.mark.regression
    def test_invalid_current_password(self):
        """This test case checks the workflow of logging into the application, clicking the change password,
        and verifying that the alert message."""


        changepassword = ChangePasswordPage(self.driver)
        changepassword.valid_login()
        self.log.info("Logged in successfully")
        changepassword.changePassword(invalidCurrentPassword, new_password, confirm_password)
        changepassword.assert_invalid()
        self.log.info("Invalid password alert message verified successfully")

    @pytest.mark.smoke
    def test_invalid_confirm_password(self):
        """This test case checks the workflow of logging into the application, clicking the change password,
        and verifying that the alert message."""

        self.log.info("Starting test_invalid_confirm_password")

        changepassword = ChangePasswordPage(self.driver)
        changepassword.valid_login()
        self.log.info("Logged in successfully")
        changepassword.changePassword(current_password, new_password, invalidConfirmPassword)
        changepassword.assert_alert()
        self.log.info("Invalid confirm password alert message verified successfully")
