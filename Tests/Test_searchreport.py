import pytest
from Pages import PIMPage
from Utility import Excel_Reader,console_logger
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")

class TestReport:
    log = console_logger.get_logger()
    @pytest.mark.smoke
    @pytest.mark.parametrize("report_name", Excel_Reader.get_data("E:\gitpytest_clone\Pytest_OrangeHRM\ExcelFiles\Report.xlsx", "Report"))
    def test_searchreport(self, report_name):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        self.log.info("PIM button is clicked")
        pim.report_button()
        self.log.info("report button is clicked")
        pim.report_search(report_name)
        self.log.info("report needed to searched is given")
        pim.search()
        self.log.info("Report is searched")
        pim.valid_assert()
        self.log.info("Report is fetched successfully")