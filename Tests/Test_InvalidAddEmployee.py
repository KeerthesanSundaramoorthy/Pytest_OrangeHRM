import pytest
from Pages import PIMPage
from Utility import Excel_Reader,console_logger
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("fname,mname,lname,emp_id", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\ExcelFiles\\Invalid_Add_Employee.xlsx", "InvalidAddEmployee"))

class TestValidAddEmployee:
    log = console_logger.get_logger()
    @pytest.mark.smoke
    def test_InvalidvalidAddEmp(self, fname, mname, lname,emp_id):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        self.log.info("PIM button is clicked")
        pim.add_employee_button()
        self.log.info("Add employee button is clicked")
        pim.add_employee(fname, mname, lname,emp_id)
        self.log.info("First_name,Middle_name,Last_name,Emp_id is sent to add the employee")
        pim.save_button()
        self.log.info("Save button is clicked")
        pim.unsuccessful_message()
        self.log.info("Unsuccesfull add")