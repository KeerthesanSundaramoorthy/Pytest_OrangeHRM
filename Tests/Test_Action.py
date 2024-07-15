"""Author: Keerthesan (Expleo)"""
import pytest
from Utility import console_logger
from Pages.DashboardPage import DashboardPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestActions:

    """    TestActions class contains test methods to perform and validate various actions on the dashboard page.   """

    log = console_logger.get_logger()
   
    @pytest.mark.smoke
    def test_work(self):

        """This test case checks the workflow of logging into the application, clicking the clock icon,
        and verifying that the Punch Out page is opened."""

        dashboard = DashboardPage(self.driver)
        dashboard.valid_login()
        self.log.info("Successfully logged into the application")
        dashboard.click_clock()
        self.log.info("Successfully clicked the clock icon in the dashboard page")
        assert dashboard.assert_punch()
        self.log.info("Punch Out page is opened and verified successfully")
   
    @pytest.mark.retest
    def test_pending(self):

        """This test case checks the workflow of logging into the application, clicking the Pending Self Review,
        and verifying that the Performance page is opened."""

        dashboard = DashboardPage(self.driver)
        dashboard.valid_login()
        self.log.info("Successfully logged into the application")
        dashboard.pending_review()
        self.log.info("Successfully clicked the Pending Self Review")
        assert dashboard.assert_performance()
        self.log.info("Performance page is opened and verified successfully")

    @pytest.mark.retest
    def test_candidates(self):

        """This test case checks the workflow of logging into the application, clicking the Candidate to Interview,
        and verifying that the Recruitment page is opened."""

        dashboard = DashboardPage(self.driver)
        dashboard.valid_login()
        self.log.info("Successfully logged into the application")
        dashboard.remaining_review()
        self.log.info("Successfully clicked the Candidate to Interview")
        assert dashboard.assert_recruitment()
        self.log.info("Recruitment page is opened and verified successfully")

