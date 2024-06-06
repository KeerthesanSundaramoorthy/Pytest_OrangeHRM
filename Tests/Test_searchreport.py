import pytest,time
from Pages import PIMPage
from Utility import ExcelReader
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")

class TestReport:
    @pytest.mark.parametrize("report_name", ExcelReader.get_data("E:\Clone_pytest\Pytest_OrangeHRM\ExcelFiles\Report.xlsx", "Report"))
    def test_searchreport(self, report_name):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        pim.report_button()
        pim.report_search(report_name)
        pim.search()