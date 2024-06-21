import pytest
from Pages import RecruitPage,PIMPage
from Tests import Test_ValidLogin
from Utility import console_logger
@pytest.mark.usefixtures("setup_and_teardown")
class TestVacancy:
    log = console_logger.get_logger()
    @pytest.mark.smoke
    def test_vacancy(self):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        pim=PIMPage.PIM_Page(self.driver)
        recruit = RecruitPage.RecruitPage(self.driver)
        recruit.recruitment_icon()
        self.log.info("Recruiment button is clicked")
        recruit.vacancy_icon_btn()
        self.log.info("Vacancies button is clicked")
        recruit.vacancy_dropdown()
        self.log.info("vacancy field is filled")
        recruit.vacancy_status_dropdown()
        self.log.info("Status field is filled")
        pim.search()
        self.log.info("Search button is clicked")
        pim.valid_assert()
        self.log.info("Successfull search")

    @pytest.mark.regression
    def test_deletelist(self):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        recruit = RecruitPage.RecruitPage(self.driver)
        recruit.recruitment_icon()
        self.log.info("Recruiment button is clicked")
        recruit.vacancy_icon_btn()
        self.log.info("Vacancies button is clicked")
        pim.delete_icon()
        self.log.info("Delete icon is clicked")
        pim.click_yes_btn()
        self.log.info("Yes button is clicked")
        pim.assert_delete()
        self.log.info("Successfully deleted")
   
    @pytest.mark.regression
    def test_editemp(self):
        Test_ValidLogin.TestLogin.test_valid_login(self)
        self.log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        recruit = RecruitPage.RecruitPage(self.driver)
        recruit.recruitment_icon()
        self.log.info("Recruiment button is clicked")
        recruit.vacancy_icon_btn()
        self.log.info("Vacancies button is clicked")
        pim.edit_btn()
        self.log.info("Edit icon is clicked")
        pim.edit_assert()
        self.log.info("Edit is successfully done")
