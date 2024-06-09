import pytest,time
from Pages import RecruitPage,PIMPage
from Tests import Test_ValidLogin
from Utility import console_logger

@pytest.mark.usefixtures("setup_and_teardown")


class TestCandidate:
    @pytest.mark.retest
    def test_candidate(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        pim=PIMPage.PIM_Page(self.driver)
        recruit = RecruitPage.RecruitPage(self.driver)
        recruit.recruitment_icon()
        log.info("Recruiment button is clicked")
        recruit.candidate_icon_btn()
        log.info("Candidate buton is clicked")
        recruit.vacancy_dropdown()
        log.info("Vacancy field is filled")
        recruit.status_dropdown()
        log.info("Status field is filled")
        pim.search()
        log.info("search button is clicked")
        pim.valid_assert()
        log.info("Successfull search")

    @pytest.mark.regression
    def test_delete(self):
        log = console_logger.get_logger()
        Test_ValidLogin.TestLogin.test_valid_login(self)
        log.info("Login is successfull")
        pim = PIMPage.PIM_Page(self.driver)
        recruit = RecruitPage.RecruitPage(self.driver)
        recruit.recruitment_icon()
        log.info("Recruiment button is clicked")
        recruit.candidate_icon_btn()
        log.info("Candidate buton is clicked")
        pim.delete_icon()
        log.info("Delete icon is clicked")
        pim.click_yes_btn()
        log.info("Yes button is clicked")
        pim.assert_delete()
        log.info("Successfully deleted")
