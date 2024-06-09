from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PIM_Page(BasePage):

    def __init__(self, driver):
       super().__init__(driver) 

    #Add Employee
    #PIM_Button_xpath = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]"
    PIM_Button_xpath =  "(//li)[2]"
    Add_Employee_Button = "//a[text()='Add Employee']"
    fname_xpath = "//input[@name='firstName']"
    mname_xpath = "//input[@name='middleName']"
    lname_xpath = "//input[@name='lastName']"
    emp_id_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"

    #Employee List
    Employee_list_xpath = "(//a[@class='oxd-topbar-body-nav-tab-item'])[1]"
    Employee_Name_xpath = "(//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']//input)[1]"
    Dropdown_xpath = "//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1]"
    Employee_Id_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    Status_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1])"
    no_record_xpath = "//span[@class='oxd-text oxd-text--span']"
   
    #common 
    save_xpath = "//button[@type='submit']"
    success_message_xpath= "(//div[@class='oxd-toast-content oxd-toast-content--success']//p)[1]"
    PIM_page_xpath = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"
    missing_field_xpath = "//p[@class='oxd-text oxd-text--p orangehrm-form-hint']"
    search_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    reset_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']"

    #delete locators
    delete_xpath = "(//button/i[@class='oxd-icon bi-trash'])[5]"
    yes_del_btn = "(//div[@class='orangehrm-modal-footer']//button)[2]"
    success_delete = "//p[text()='Successfully Deleted']"

    #edit locators
    edit_icon_xpath = "(//i[@class='oxd-icon bi-pencil-fill'])[2]"
    personal_page_xpath = "//a[@class='orangehrm-tabs-item --active']"

    #Reports
    report_button_xpath = "(//a[@class='oxd-topbar-body-nav-tab-item'])[3]"
    report_name_xpath =  "//input[@placeholder='Type for hints...']"
    report_error  =  "No Records Found"
    
    #PIM Button Click
    def PIM_button(self):
        self.find(By.XPATH,self.PIM_Button_xpath).click()

    #Employee List
    def employee_list_button(self):
        self.find(By.XPATH,self.Employee_list_xpath).click()

    def employee_name(self,emp_name):
        self.send_key(By.XPATH,self.Employee_Name_xpath,emp_name)
    
    def employee_id(self,emp_idd):
        self.send_key(By.XPATH,self.Employee_Id_xpath,str(emp_idd))

    def invalid_assert(self):
        actual = self.find(By.XPATH,self.no_record_xpath).text
        assert actual.__eq__("No Records Found") 

    def valid_assert(self):
        actual = self.find(By.XPATH,self.no_record_xpath).text
        assert actual.__eq__("No Records Found") == False
    
    #Add Button
    def add_employee_button(self):
        self.find(By.XPATH,self.Add_Employee_Button).click()

    def add_employee(self, fname, mname, lname, emp_id):
        try:
            if fname is not None:
                self.send_key(By.XPATH, self.fname_xpath, fname)
            if mname is not None:
                self.send_key(By.XPATH, self.mname_xpath, mname)
            if lname is not None:
                self.send_key(By.XPATH, self.lname_xpath, lname)
            if emp_id is not None:
                emp_id_element = self.driver.find_element(By.XPATH, self.emp_id_xpath)
                emp_id_element.clear()
                self.send_key(By.XPATH, self.emp_id_xpath, str(emp_id))
            else:
                print("Employee ID is None, skipping the ID field.")
        except Exception as e:
            print(f"An error occurred while adding the employee: {e}")


    def save_button(self):
        self.find(By.XPATH,self.save_xpath).click()

    def success_message(self):      
      '''added_message = self.driver.find_element(By.XPATH,"(//div[@class='oxd-toast-content oxd-toast-content--success']//p)[1]")
      assert added_message.is_displayed(), "Success"'''
      added_message = self.driver.find_element(By.XPATH,self.PIM_page_xpath)
      assert added_message.is_displayed(), "PIM"

    def unsuccessful_message(self):
        error_message = self.driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-form-hint']")
        assert error_message.is_displayed(), "* Required"

       
    #Reports
    def report_button(self):
        self.find(By.XPATH,self.report_button_xpath).click()

    def report_search(self, report_name):
        if isinstance(report_name, list):
            report_name = ' '.join(map(str, report_name))
        else:
            report_name = str(report_name)
    
        self.send_key(By.XPATH, self.report_name_xpath, report_name)
        name_locator = f"//span[text()='{report_name}']"
        name_click = self.wait.until(ec.element_to_be_clickable((By.XPATH, name_locator)))
        name_click.click()

    def report_invalidsearch(self,report_name):
        if isinstance(report_name, list):
            report_name = ' '.join(map(str, report_name))
        else:
            report_name = str(report_name)
    
        self.send_key(By.XPATH, self.report_name_xpath, report_name)
        no_records_locator = "//span[text()='No Records Found']"
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, no_records_locator)))
            no_records_element = self.driver.find_element(By.XPATH, no_records_locator)
            if no_records_element.is_displayed():
                no_records_element.click()
        finally:
            invalid_message = self.driver.find_element(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
            assert invalid_message.is_displayed(), "Invalid"

    def search(self):
        self.find(By.XPATH,self.search_xpath).click()

    def reset(self):
        self.find(By.XPATH,self.reset_xpath).click()

    
    #To delete Record
    def delete_icon(self):
        self.find(By.XPATH,self.delete_xpath).click()

    def click_yes_btn(self):
        self.find(By.XPATH,self.yes_del_btn).click()

    def assert_delete(self):
        actual = self.find(By.XPATH,self.success_delete).text
        excepted = "Successfully Deleted"
        assert actual.__eq__(excepted)

    #edit
    def edit_btn(self):
        self.find(By.XPATH,self.edit_icon_xpath).click()

    def edit_assert(self):
        actual = "Edit Vacancy"
        expected = self.find(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']").text
        assert actual.__eq__(expected)