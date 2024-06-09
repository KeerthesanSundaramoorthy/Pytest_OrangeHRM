import pytest
from Pages import DashboardPage
from Tests import Test_ValidLogin
from Utility import console_logger

@pytest.mark.usefixtures("setup_and_teardown")

class TestQuickLaunch:
    @pytest.mark.smoke
    def test_assignleave(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        dashboard = DashboardPage.Dashboard_Page(self.driver)
        dashboard.assign_leave()
        log.info("Assign leave button is clicked")
        dashboard.leave_page_navigate()
        log.info("Page navigates successfully")

    @pytest.mark.smoke
    def test_leavelist(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        dashboard = DashboardPage.Dashboard_Page(self.driver)
        dashboard.leave_list()
        log.info("Leave list button is clicked")
        dashboard.leave_page_navigate()
        log.info("Page navigates successfully")

    @pytest.mark.smoke
    def test_timesheet(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        dashboard = DashboardPage.Dashboard_Page(self.driver)
        dashboard.timesheet_page()
        log.info("Timesheet Page button is clicked")
        dashboard.timesheet_page_navigate()
        log.info("Page navigates successfully")

    @pytest.mark.retest
    def test_applyleave(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        dashboard = DashboardPage.Dashboard_Page(self.driver)
        dashboard.apply_leave()
        log.info("Apply leave button is clicked")
        dashboard.leave_page_navigate()
        log.info("Page navigates successfully")

    @pytest.mark.retest
    def test_myleave(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        dashboard = DashboardPage.Dashboard_Page(self.driver)
        dashboard.my_leave()
        log.info("My leave button is clicked")
        dashboard.leave_page_navigate()
        log.info("Page navigates successfully")

    @pytest.mark.retest
    def test_mytimesheet(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        dashboard = DashboardPage.Dashboard_Page(self.driver)
        dashboard.my_timesheet()
        log.info("My Timesheet button is clicked")
        dashboard.timesheet_page_navigate()
        log.info("Page navigates successfully")  
