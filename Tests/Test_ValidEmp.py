import pytest,time
from Pages import PIMPage
from Utility import excelreader
from Tests import Test_Login

@pytest.mark.usefixtures("setup_and_teardown")
class TestValidAddEmployee:
    @pytest.mark.parametrize("fname,mname,lname", excelreader.get_data("E:\Clone_pytest\Clone_pytest\Pytest_OrangeHRM\ExcelFiles\Add_Employee.xlsx", "AddEmployee"))
    def test_validAddEmp(self, fname, mname, lname):
        Test_Login.TestLogin.test_valid_login(self)
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        pim.add_employee_button()
        pim.Add_Employee(fname, mname, lname)
        pim.save_button()
        pim.success_message()