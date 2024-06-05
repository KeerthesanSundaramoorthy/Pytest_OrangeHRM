import pytest,time
from Pages import PIMPage
from Utility import excelreader
from Tests import Test_Login

@pytest.mark.usefixtures("setup_and_teardown")
class TestEmployeeSearch:
    @pytest.mark.parametrize("Employee_Name", excelreader.get_data("E:\Clone_pytest\Clone_pytest\Pytest_OrangeHRM\ExcelFiles\Employee_Information.xlsx", "Employee"))
    def test_Employeesearch(self, Employee_Name):
        Test_Login.TestLogin.test_valid_login(self)
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        pim.employee_list_button()
        pim.employee_name(Employee_Name)
     