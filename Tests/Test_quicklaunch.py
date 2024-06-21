import pytest
from Pages import DashboardPage
from Tests import Test_ValidLogin
from Utility import console_logger

@pytest.mark.usefixtures("setup_and_teardown")

class TestQuickLaunch:
    log = console_logger.get_logger()
    @pytest.mark.smoke
    def test_assignleave(self):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        dashboard = DashboardPage.DashboardPage(self.driver)
        dashboard.assign_leave()
        self.log.info("Assign leave button is clicked")
        dashboard.leave_page_navigate()
        self.log.info("Page navigates successfully")

    @pytest.mark.smoke
    def test_leavelist(self):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        dashboard = DashboardPage.DashboardPage(self.driver)
        dashboard.leave_list()
        self.log.info("Leave list button is clicked")
        dashboard.leave_page_navigate()
        self.log.info("Page navigates successfully")

    @pytest.mark.smoke
    def test_timesheet(self):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        dashboard = DashboardPage.DashboardPage(self.driver)
        dashboard.timesheet_page()
        self.log.info("Timesheet Page button is clicked")
        dashboard.timesheet_page_navigate()
        self.log.info("Page navigates successfully")

    @pytest.mark.retest
    def test_applyleave(self):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        dashboard = DashboardPage.DashboardPage(self.driver)
        dashboard.apply_leave()
        self.log.info("Apply leave button is clicked")
        dashboard.leave_page_navigate()
        self.log.info("Page navigates successfully")

    @pytest.mark.retest
    def test_myleave(self):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        dashboard = DashboardPage.DashboardPage(self.driver)
        dashboard.my_leave()
        self.log.info("My leave button is clicked")
        dashboard.leave_page_navigate()
        self.log.info("Page navigates successfully")

    @pytest.mark.retest
    def test_mytimesheet(self):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        dashboard = DashboardPage.DashboardPage(self.driver)
        dashboard.my_timesheet()
        self.log.info("My Timesheet button is clicked")
        dashboard.timesheet_page_navigate()
        self.log.info("Page navigates successfully")  
