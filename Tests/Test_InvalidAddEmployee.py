import pytest,time
from Pages import PIMPage
from Utility import ExcelReader,console_logger
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("fname,mname,lname,emp_id", ExcelReader.get_data("E:\Pytest_clone\Pytest_clone\Pytest_OrangeHRM\ExcelFiles\Invalid_Add_Employee.xlsx", "InvalidAddEmployee"))

class TestValidAddEmployee:
    @pytest.mark.smoke
    def test_InvalidvalidAddEmp(self, fname, mname, lname,emp_id):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        log.info("PIM button is clicked")
        pim.add_employee_button()
        log.info("Add employee button is clicked")
        pim.add_employee(fname, mname, lname,emp_id)
        log.info("First_name,Middle_name,Last_name,Emp_id is sent to add the employee")
        pim.save_button()
        log.info("Save button is clicked")
        pim.unsuccessful_message()
        log.info("Unsuccesfull add")