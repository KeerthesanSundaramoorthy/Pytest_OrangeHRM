import pytest
from Pages import PIMPage
from Utility import ExcelReader,console_logger
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")
class TestEmployeeSearch:
    @pytest.mark.smoke
    @pytest.mark.parametrize("Employee_Name_invalid,Employee_Id", ExcelReader.get_data("E:\gitpytest_clone\Pytest_OrangeHRM\ExcelFiles\Employee_Info.xlsx", "InvalidEmployee"))
    def test_invalidemplist(self, Employee_Name_invalid,Employee_Id):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        log.info("PIM button is clicked")
        pim.employee_list_button()
        log.info("Employee list button is clicked")
        pim.employee_name(Employee_Name_invalid)
        log.info("Employee name is send")
        pim.employee_id(Employee_Id)
        log.info("Employee Id is send")
        pim.search()
        log.info("Search button is clicked")
        pim.invalid_assert()
        log.info("No Records Found is displayed")

    @pytest.mark.smoke
    @pytest.mark.parametrize("emp_name,emp_id", ExcelReader.get_data("E:\Pytest_clone\Pytest_clone\Pytest_OrangeHRM\ExcelFiles\Employee_Info.xlsx", "validlist"))
    def test_validemplist(self, emp_name,emp_id):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        log.info("PIM button is clicked")
        pim.employee_list_button()
        log.info("Employee list button is clicked")
        pim.employee_name(emp_name)
        log.info("Employee name is send")
        pim.employee_id(emp_id)
        log.info("Employee Id issend")
        pim.search()
        log.info("Search button is clicked")
        pim.valid_assert()
        log.info("Record are found")

    @pytest.mark.regression
    def test_deletelist(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        log.info("PIM button is clicked")
        pim.delete_icon()
        log.info("Delete icon is clicked")
        pim.click_yes_btn()
        log.info("Yes button is clicked")
        pim.assert_delete()
        log.info("Successfully deleted")
   
    @pytest.mark.retest
    def test_editemp(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        log.info("PIM button is clicked")
        pim.edit_btn()
        log.info("Edit icon is clicked")
        pim.edit_assert()
        log.info("Edit is done successfully")
