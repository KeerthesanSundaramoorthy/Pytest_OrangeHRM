import pytest
from Pages.LoginPage import LoginPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_valid_login(self):
        login = LoginPage(self.driver) #object reference
        username = utility_file.get_config("valid login details","username")
        password = utility_file.get_config("valid login details","password")
        login.login(username,password)