import pytest,time
from Pages import PIMPage
from Utility import excelreader
from Tests import Test_Login

@pytest.mark.usefixtures("setup_and_teardown")
class TestReport:
    @pytest.mark.parametrize("report_name", excelreader.get_data("E:\Clone_pytest\Clone_pytest\Pytest_OrangeHRM\ExcelFiles\Reports.xlsx", "Report"))
    def test_searchreport(self, report_name):
        Test_Login.TestLogin.test_valid_login(self)
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        pim.report_search(report_name)
        pim.search()