import pytest
from Pages import DashboardPage
from Tests import Test_Login
from Tests import Test_Login

@pytest.mark.usefixtures("setup_and_teardown")
class TestQuickLaunch:
    def test_assign_leave(self):
        Test_Login.TestLogin.test_valid_login(self)
        dashboard_page =DashboardPage.Dashboard_Page(self)
        dashboard_page.assign_leave()
