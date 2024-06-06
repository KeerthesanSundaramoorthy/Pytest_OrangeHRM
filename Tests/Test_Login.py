#test login

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.LoginPage import LoginPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_valid_login(self):
        login = LoginPage(self.driver) 
        username = utility_file.get_config("valid login details","username")
        password = utility_file.get_config("valid login details","password")
        login.login(username,password)