import pytest,time
from Pages import PIMPage
from Utility import ExcelReader,console_logger
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("fname,mname,lname,emp_id", ExcelReader.get_data("E:\gitpytest_clone\Pytest_OrangeHRM\ExcelFiles\Add_Employee.xlsx", "AddEmployee"))


class TestValidAddEmployee:
    @pytest.mark.smoke
    def test_validAddEmp(self, fname, mname, lname,emp_id):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successful")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        log.info("PIM button is clicked")
        pim.add_employee_button()
        log.info("Add Employee button is clicked")
        pim.add_employee(fname, mname, lname,emp_id)
        log.info("First_name,Middle_name,Last_name are sent to add value")
        pim.save_button()
        log.info("Save button is clicked")
        pim.success_message()
        log.info("Successfull added")
        