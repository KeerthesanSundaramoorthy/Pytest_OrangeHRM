import pytest
from Pages import PIMPage
from Utility import ExcelReader,console_logger
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")

class TestReport:
    @pytest.mark.smoke
    @pytest.mark.parametrize("report_name", ExcelReader.get_data("E:\gitpytest_clone\Pytest_OrangeHRM\ExcelFiles\Report.xlsx", "Report"))
    def test_searchreport(self, report_name):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        log.info("PIM button is clicked")
        pim.report_button()
        log.info("report button is clicked")
        pim.report_search(report_name)
        log.info("report needed to searched is given")
        pim.search()
        log.info("Report is searched")
        pim.valid_assert()
        log.info("Report is fetched successfully")