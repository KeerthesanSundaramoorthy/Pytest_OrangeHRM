import pytest
from Pages import PIMPage
from Utility import Excel_Reader, console_logger
from Tests import Test_ValidLogin
from selenium.common.exceptions import TimeoutException

@pytest.mark.usefixtures("setup_and_teardown")
class TestReport:
    log = console_logger.get_logger()

    @pytest.mark.smoke
    @pytest.mark.parametrize("report_name", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\ExcelFiles\\Report.xlsx", "Report"))
    def test_searchreport(self, report_name):
        try:
            Test_ValidLogin.TestLogin.test_valid_login(self)
            self.log.info("Login is successful")
            
            pim = PIMPage.PIM_Page(self.driver)
            pim.PIM_button()
            self.log.info("PIM button is clicked")
            
            pim.report_button()
            self.log.info("Report button is clicked")
            
            pim.report_search(report_name)
            self.log.info(f"Report to be searched: {report_name}")
            
            pim.search()
            self.log.info("Search button is clicked")
            
            pim.valid_assert()
            self.log.info("Report is fetched successfully")
        
        except TimeoutException as e:
            self.log.error(f"TimeoutException occurred: {str(e)}")
            pytest.fail("Test failed due to TimeoutException")
        except Exception as e:
            self.log.error(f"An error occurred: {str(e)}")
            pytest.fail("Test failed due to an unexpected exception")