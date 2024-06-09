import pytest
from Pages import RecruitPage,PIMPage
from Tests import Test_ValidLogin
from Utility import console_logger
@pytest.mark.usefixtures("setup_and_teardown")
class TestVacancy:
    @pytest.mark.smoke
    def test_vacancy(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        pim=PIMPage.PIM_Page(self.driver)
        recruit = RecruitPage.RecruitPage(self.driver)
        recruit.recruitment_icon()
        log.info("Recruiment button is clicked")
        recruit.vacancy_icon_btn()
        log.info("Vacancies button is clicked")
        recruit.vacancy_dropdown()
        log.info("vacancy field is filled")
        recruit.vacancy_status_dropdown()
        log.info("Status field is filled")
        pim.search()
        log.info("Search button is clicked")
        pim.valid_assert()
        log.info("Successfull search")

    @pytest.mark.regression
    def test_deletelist(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        recruit = RecruitPage.RecruitPage(self.driver)
        recruit.recruitment_icon()
        log.info("Recruiment button is clicked")
        recruit.vacancy_icon_btn()
        log.info("Vacancies button is clicked")
        pim.delete_icon()
        log.info("Delete icon is clicked")
        pim.click_yes_btn()
        log.info("Yes button is clicked")
        pim.assert_delete()
        log.info("Successfully deleted")
   
    @pytest.mark.regression
    def test_editemp(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        recruit = RecruitPage.RecruitPage(self.driver)
        recruit.recruitment_icon()
        log.info("Recruiment button is clicked")
        recruit.vacancy_icon_btn()
        log.info("Vacancies button is clicked")
        pim.edit_btn()
        log.info("Edit icon is clicked")
        pim.edit_assert()
        log.info("Edit is successfully done")
