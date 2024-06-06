import pytest,time
from Pages import PIMPage
from Utility import ExcelReader
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("fname,mname,lname,emp_id", ExcelReader.get_data("E:\gitpytest_clone\Pytest_OrangeHRM\ExcelFiles\Add_Employee.xlsx", "AddEmployee"))


class TestValidAddEmployee:
    def test_validAddEmp(self, fname, mname, lname,emp_id):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        pim.add_employee_button()
        pim.Add_Employee(fname, mname, lname,emp_id)
        pim.save_button()
        pim.success_message()