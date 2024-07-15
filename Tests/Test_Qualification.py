"""Author: Keerthesan (Expleo)"""
import pytest
from Utility import console_logger
from Pages.QualificationsPage import QualificationPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestQualification:

    """TestQualification class contains test methods to verify the qualification details is added on the qualification page."""
    
    log = console_logger.get_logger()

    @pytest.mark.smoke
    def test_qualification(self):

        """ This test case checks the workflow of logging into the application, navigating to the Qualification page,
        adding a new qualification, and verifying that the qualification is saved successfully."""

        qualify = QualificationPage(self.driver)
        company = utility_file.get_config("Qualification Details","company")
        title = utility_file.get_config("Qualification Details","title")
        from_date = utility_file.get_config("Qualification Details","from_date")
        to_date = utility_file.get_config("Qualification Details","to_date")
        comment = utility_file.get_config("Qualification Details","comment")
        qualify.valid_login()
        self.log.info("Successfully logged into the application")
        qualify.qualification()
        self.log.info("Qualification is clicked from the list successfully")
        qualify.click_add()
        self.log.info("Add button is clicked")
        qualify.company_name(company)
        self.log.info("Company name is typed in the Company name text box") 
        qualify.job_title(title)
        self.log.info("Job Title is typed in the appropriate text box")
        qualify.from_date(from_date)
        self.log.info("From date is typed in the appropriate text box")
        qualify.to_date(to_date)
        self.log.info("To Date is typed in the appropriate text box")
        qualify.comment(comment)
        self.log.info("Comment is typed in the appropriate text box")
        qualify.click_save()
        self.log.info("Save button is clicked") 
        assert qualify.assert_myinfo()
        self.log.info("Successfully Saved message is seen and verified")

    @pytest.mark.valid
    def test_man_qualification(self):
        
        """ This test case checks the workflow of logging into the application, navigating to the Qualification page,
        adding a new qualification with only the Company name and Job Title, and verifying that the qualification is saved successfully."""

        qualify = QualificationPage(self.driver)
        company = utility_file.get_config("Qualification Details","company")
        title = utility_file.get_config("Qualification Details","title")
        qualify.valid_login()
        self.log.info("Successfully logged into the application")
        qualify.qualification()
        self.log.info("Qualification is clicked from the list successfully")
        qualify.click_add()
        self.log.info("Add button is clicked")
        qualify.company_name(company)
        self.log.info("Company name is typed in the Company name text box") 
        qualify.job_title(title)
        self.log.info("Job Title is typed in the appropriate text box") 
        qualify.click_save()
        self.log.info("Save button is clicked") 
        assert qualify.assert_myinfo()
        self.log.info("Successfully Saved message is seen and verified")