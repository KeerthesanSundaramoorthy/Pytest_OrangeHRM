import pytest,time
from Pages import PIMPage
from Utility import Excel_Reader,console_logger
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("fname,mname,lname,emp_id", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\ExcelFiles\\Add_Employee.xlsx", "AddEmployee"))


class TestValidAddEmployee:
    log = console_logger.get_logger()
    @pytest.mark.smoke
    def test_validAddEmp(self, fname, mname, lname,emp_id):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successful")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        self.log.info("PIM button is clicked")
        pim.add_employee_button()
        self.log.info("Add Employee button is clicked")
        pim.add_employee(fname, mname, lname,emp_id)
        self.log.info("First_name,Middle_name,Last_name are sent to add value")
        pim.save_button()
        self.log.info("Save button is clicked")
        pim.success_message()
        self.log.info("Successfull added")
        