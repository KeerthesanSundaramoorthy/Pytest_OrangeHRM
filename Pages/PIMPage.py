from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

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
    Employee_Name_xpath = "(//input[@placeholder='Type for hints...''])"
    Dropdown_xpath = "//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1]"
    Employee_Id_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    Status_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1])"
   
    #common 
    save_xpath = "//button[@type='submit']"
    success_message_xpath= "(//div[@class='oxd-toast-content oxd-toast-content--success']//p)[1]"
    PIM_page_xpath = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"
    missing_field_xpath = "//p[@class='oxd-text oxd-text--p orangehrm-form-hint']"
    search_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    reset_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']"

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
        self.send_key(By.XPATH,self.Employee_Id_xpath,emp_idd)
    
    #Add Button
    def add_employee_button(self):
        self.find(By.XPATH,self.Add_Employee_Button).click()

    def Add_Employee(self,fname,mname,lname,emp_id):
        '''self.send_key(By.XPATH,self.fname_xpath,fname)
        self.send_key(By.XPATH,self.mname_xpath,mname)
        self.send_key(By.XPATH,self.lname_xpath,lname)'''
        if fname is not None:
            self.send_key(By.XPATH, self.fname_xpath, fname)
        if mname is not None:
            self.send_key(By.XPATH, self.mname_xpath, mname)
        if lname is not None:
            self.send_key(By.XPATH, self.lname_xpath, lname)
        self.send_key(By.XPATH,self.emp_id_xpath,str(emp_id))

    def save_button(self):
        self.find(By.XPATH,self.save_xpath).click()

    def success_message(self):      
      added_message = self.driver.find_element(By.XPATH,"(//div[@class='oxd-toast-content oxd-toast-content--success']//p)[1]")
      assert added_message.is_displayed(), "Success"

    def unsuccessful_message(self):
        '''unsuccess_message_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.missing_field_xpath))
        unsuccess_message_text = unsuccess_message_element.text
        assert unsuccess_message_text == "* Required", f"Expected 'Success' but got '{unsuccess_message_text}'"'''
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

    def search(self):
        self.find(By.XPATH,self.search_xpath).click()

    def reset(self):
        self.find(By.XPATH,self.reset_xpath).click()

    