from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class RecruitPage(BasePage):
    def __init__(self, driver):
       super().__init__(driver)

    #Recruitment Icon Locator
    recruitment_icon_xpath = "(//li[@class='oxd-main-menu-item-wrapper']//span)[5]"

    #Candidate
    Candidate_icon_xpath  =  "//a[text()='Candidates']"
    candidate_name_xpath = "(//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']//input)"
    select_xpath = "(//div[@class='oxd-select-text-input'])[2]"
    status_xpath = "//span[text()='Application Initiated']"
    vacancy_xpath = "//span[text()='Senior QA Lead']"
    statuslocat_xpath = "(//div[@class='oxd-select-text-input'])[4]"

    #Vacancy 
    vacancies_icon = "//a[text()='Vacancies']"
    vac_status_xpath = "//span[text()='Active']"


    def recruitment_icon(self):
        self.find(By.XPATH,self.recruitment_icon_xpath).click()

    def candidate_icon_btn(self):
        self.find(By.XPATH,self.Candidate_icon_xpath).click()

    def vacancy_dropdown(self):
        self.click(By.XPATH, self.select_xpath)
        emp = self.wait.until(ec.element_to_be_clickable((By.XPATH, self.vacancy_xpath)))
        emp.click()

    def status_dropdown(self):
        self.click(By.XPATH,self.statuslocat_xpath)
        status =self.wait.until(ec.element_to_be_clickable((By.XPATH,self.status_xpath)))
        status.click()

    def vacancy_icon_btn(self):
        self.find(By.XPATH,self.vacancies_icon).click()

    def vacancy_status_dropdown(self):
        self.click(By.XPATH,self.statuslocat_xpath)
        status =self.wait.until(ec.element_to_be_clickable((By.XPATH,self.vac_status_xpath)))
        status.click()
