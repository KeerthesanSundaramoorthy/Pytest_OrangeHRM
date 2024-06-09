import pytest
from Pages import DashboardPage
from Tests import Test_ValidLogin
from Utility import console_logger

@pytest.mark.usefixtures("setup_and_teardown")


class TestLeaveList:
    @pytest.mark.retest
    def test_emp_leavelist(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        dashboard = DashboardPage.Dashboard_Page(self.driver)
        print(dashboard.emp_leavelist())
        log.info("Print total number of people on leave")