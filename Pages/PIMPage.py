from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIM_Page(BasePage):

    def __init__(self, driver):
       super().__init__(driver) 

    #Add Employee
    PIM_Button_xpath = (By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]")
    #PIM_Button_xpath =  "(//li)[2]"
    Add_Employee_Button = (By.XPATH,"//a[text()='Add Employee']")
    fname_xpath = (By.XPATH,"//input[@name='firstName']")
    mname_xpath = (By.XPATH,"//input[@name='middleName']")
    lname_xpath = (By.XPATH,"//input[@name='lastName']")

    #Employee List
    Employee_list_xpath = (By.XPATH,"//a[text()='Employee List']")
    Employee_Name_xpath = (By.XPATH,"(//input[@placeholder='Type for hints...''])")
    Dropdown_xpath = (By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1]")
    Employee_Id_xpath = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    Status_xpath = (By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active'][normalize-space()='-- Select --'])[1])")
   
    #common 
    save_xpath = (By.XPATH,"//button[@type='submit']")
    success_message_xpath= (By.XPATH,"(//div[@class='oxd-toast-content oxd-toast-content--success']//p)[1]")
    PIM_page_xpath =(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    missing_field_xpath = (By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-form-hint']")
    search_xpath = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
    reset_xpath = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--ghost']")

    #Reports
    report_button_xpath = (By.XPATH,"(//a[@class='oxd-topbar-body-nav-tab-item'])[3]")
    report_name_xpath =  (By.XPATH,"//input[@placeholder='Type for hints...']")
    report_error  =  "No Records Found"
    
    def PIM_button(self):
        self.click(*self.PIM_Button_xpath)

    #Employee List
    def employee_list_button(self):
        self.click(*self.Employee_list_xpath)

    def employee_name(self,emp_name1):
        emp_name = self.find(By.XPATH,self.Employee_Name_xpath)
        self.send_key(*self.Employee_Name_xpath,emp_name1)
        emp = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Qwetry Qwetry Lname']")))
        emp.click()
    
    #Add Button
    def add_employee_button(self):
        self.click(*self.Add_Employee_Button)

    def Add_Employee(self,fname,mname,lname):
        self.send_key(*self.fname_xpath,fname)
        self.send_key(*self.mname_xpath,mname)
        self.send_key(*self.lname_xpath,lname)

    def save_button(self):
        self.click(*self.save_xpath)

    def success_message(self):
       
       #success message
       success_message_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_message_xpath))
       success_message_text = success_message_element.text
       assert success_message_text == "Success", f"Expected 'Success' but got '{success_message_text}'"
       
       #PIM
       page_navigate_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PIM_page_xpath))
       PIM_message_text = page_navigate_element.text
       assert PIM_message_text == "PIM", f"Expected 'PIM' but got '{PIM_message_text}'"

    def unsuccessful_message(self):
        unsuccess_message_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.missing_field_xpath))
        unsuccess_message_text = unsuccess_message_element.text
        assert unsuccess_message_text == "* Required", f"Expected 'Success' but got '{unsuccess_message_text}'"

       
    #Reports
    def report_search(self,report_name):
        self.click(*self.report_button_xpath)
        self.send_key(*self.report_name_xpath,report_name)
        select_report_xpath = (By.XPATH, f"//span[text()='PIM Sample Report']")
        '''select_report_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(select_report_xpath))
        select_report_element.click()'''
        try:
            select_report_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(select_report_xpath))
            print(f"Found report element: {select_report_element}")  # Debug statement
            select_report_element.click()
        except Exception as e:
            print(f"Error finding report element: {e}")

    def search(self):
        self.click(*self.search_xpath)

    def reset(self):
        self.click(*self.reset_xpath)

    