import pytest,time
from Pages import PIMPage
from Utility import ExcelReader
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("Employee_Name,Employee_Id", ExcelReader.get_data("E:\gitpytest_clone\Pytest_OrangeHRM\ExcelFiles\Employee_Info.xlsx", "Employee"))
class TestEmployeeSearch:
    def test_emplist(self, Employee_Name,Employee_Id):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        pim.employee_list_button()
        pim.employee_name(Employee_Name)
        pim.employee_id(Employee_Id)
        pim.search()