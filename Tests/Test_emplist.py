import pytest
from Pages import PIMPage
from Utility import Excel_Reader,console_logger
from Tests import Test_ValidLogin

@pytest.mark.usefixtures("setup_and_teardown")
class TestEmployeeSearch:
    log = console_logger.get_logger()
    @pytest.mark.smoke
    @pytest.mark.parametrize("Emp_id", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\ExcelFiles\\Invalid_searchemp.xlsx", "Emp"))
    def test_invalidemplist(self,Emp_id):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        self.log.info("PIM button is clicked")
        pim.employee_list_button()
        self.log.info("Employee list button is clicked")
        '''pim.employee_name(Employee_Name_invalid)
        self.log.info("Employee name is send")'''
        pim.employee_id(Emp_id)
        self.log.info("Employee Id is send")
        pim.search()
        self.log.info("Search button is clicked")
        pim.invalid_assert()
        self.log.info("No Records Found is displayed")

    @pytest.mark.smoke
    @pytest.mark.parametrize("emp_name,emp_id", Excel_Reader.get_data("C:\\Users\\SM\\Downloads\\Pytest_10-07-24\\Pytest_Clone_3\\Pytest_OrangeHRM\\ExcelFiles\\Employee_Info.xlsx", "Employee"))
    def test_validemplist(self, emp_name,emp_id):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        self.log.info("PIM button is clicked")
        pim.employee_list_button()
        self.log.info("Employee list button is clicked")
        pim.employee_name(emp_name)
        self.log.info("Employee name is send")
        pim.employee_id(emp_id)
        self.log.info("Employee Id issend")
        pim.search()
        self.log.info("Search button is clicked")
        pim.valid_assert()
        self.log.info("Record are found")

    @pytest.mark.regression
    def test_deletelist(self):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        self.log.info("PIM button is clicked")
        pim.delete_icon()
        self.log.info("Delete icon is clicked")
        pim.click_yes_btn()
        self.log.info("Yes button is clicked")
        pim.assert_delete()
        self.log.info("Successfully deleted")
   
    @pytest.mark.retest
    def test_editemp(self):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        pim.PIM_button()
        self.log.info("PIM button is clicked")
        pim.edit_btn()
        self.log.info("Edit icon is clicked")
        pim.edit_assert_search()
        self.log.info("Edit is done successfully")
