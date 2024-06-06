import pytest,time
from Pages import PIMPage
from Utility import ExcelReader
from Pages import BasePage
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("fname,mname,lname,emp_id", ExcelReader.get_data("E:\gitpytest_clone\Pytest_OrangeHRM\ExcelFiles\Invalid_Add_Employee.xlsx", "InvalidAddEmployee"))


class TestValidAddEmployee:
    def test_InvalidvalidAddEmp(self, fname, mname, lname,emp_id):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        pim.add_employee_button()
        pim.Add_Employee(fname, mname, lname,emp_id)
        pim.save_button()
        pim.unsuccessful_message()