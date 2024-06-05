import pytest
from Pages.UserPage import UserPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestUser:
    @pytest.mark.valid
    def test_valid_search(self):
        user_page = UserPage(self.driver)
        user_page.valid_login()
        user_page.user_management()
        username1 = utility_file.get_config("valid user details","username1")
        emp_name = utility_file.get_config("valid user details","emp_name")
        user_page.username(username1) 
        user_page.ess_userrole()
        user_page.employee_name(emp_name)
        user_page.select_status()
        user_page.search()
        assert user_page.search_assert()

    def test_partial_search(self):
        user_page = UserPage(self.driver)
        user_page.valid_login()
        user_page.user_management()
        username1 = utility_file.get_config("partial user details","username1")
        user_page.username(username1) 
        user_page.select_status()
        user_page.search()
        assert user_page.search_assert()

    @pytest.mark.invalid
    def test_invalid_search(self):
        user_page = UserPage(self.driver)
        user_page.valid_login()
        user_page.user_management()
        username1 = utility_file.get_config("invalid user details","username1")
        user_page.username(username1) 
        user_page.admin_userrole()
        user_page.search()
        assert user_page.search_assert()