"""Author: Suvetha (Expleo)"""
import pytest
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Utility import Excel_Reader, console_logger

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("username,password", Excel_Reader.get_data("E:\gitpytest_clone\Pytest_OrangeHRM\Excel_Files\Invalid_LoginData.xlsx", "loginInvalid"))
class TestLogin:
    """TestLogin class contains test methods for invalid login."""

    log = console_logger.get_logger()

    def test_invalid_login(self, username, password):
        """This test case checks the workflow of logging into the application,
        verifying the invalid login."""

        login = LoginPage(self.driver)
        login.login(username, password)
        error_message = self.driver.find_element(By.XPATH, "//p[text()='Invalid credentials']")
        assert error_message.is_displayed(), "Error message for invalid login is not displayed"
        self.log.info("Invalid login error message verified successfully")
