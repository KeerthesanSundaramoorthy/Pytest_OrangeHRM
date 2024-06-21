"""Author: Keerthesan (Expleo)"""
import pytest
from Utility import console_logger
from Pages.JobPage import JobPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestJob:

    """ TestJob class contains test methods to perform and validate the new job is added on the job page."""

    log = console_logger.get_logger()
    
    @pytest.mark.smoke
    def test_add_job(self):

        """ This test case checks the workflow of logging into the application, navigating to the job section,
        adding a new job with valid details, and verifying that the job is successfully saved."""

        job = JobPage(self.driver)
        title = utility_file.get_config("valid job details","job_title")
        desc = utility_file.get_config("valid job details","job_descr")
        note = utility_file.get_config("valid job details","job_note")
        job.valid_login()
        self.log.info("Successfully logged into the application")
        job.job_functions()
        self.log.info("Jobs is clicked from the drop down successfully")
        job.add()
        self.log.info("Add button is clicked")
        job.job_title(title)
        self.log.info("Job title is typed in the appropriate text box")
        job.job_description(desc)
        self.log.info("Job description is typed in the appropriate text box")
        job.job_note(note)
        self.log.info("Job note is typed in the appropriate text box")
        job.click_save()
        self.log.info("Save button is clicked") 
        assert job.assert_job()
        self.log.info("Successfully Saved message is seen and verified")

    @pytest.mark.regression
    def test_cancel(self):
        
        """This test case checks the workflow of logging into the application, navigating to the job section,
        starting to add a new job with valid details, cancelling the action, and verifying that the previous page is loaded."""

        job = JobPage(self.driver)
        title = utility_file.get_config("valid job details","job_title")
        desc = utility_file.get_config("valid job details","job_descr")
        note = utility_file.get_config("valid job details","job_note")
        job.valid_login()
        self.log.info("Successfully logged into the application")
        job.job_functions()
        self.log.info("Jobs is clicked from the drop down successfully")
        job.add()
        self.log.info("Add button is clicked")
        job.job_title(title)
        self.log.info("Job title is typed in the appropriate text box")
        job.job_description(desc)
        self.log.info("Job description is typed in the appropriate text box")
        job.job_note(note)
        self.log.info("Job note is typed in the appropriate text box")
        job.click_cancel()
        self.log.info("Cancel button is clicked") 
        assert job.assert_previous()
        self.log.info("Previous Page is loaded and verified")

    @pytest.mark.smoke
    def test_partial_job(self):
        
        """This test case checks the workflow of logging into the application, navigating to the job section,
        adding a new job with partial details, and verifying that the job is successfully saved."""

        job = JobPage(self.driver)
        title = utility_file.get_config("partial job details","job_title")
        job.valid_login()
        self.log.info("Successfully logged into the application")
        job.job_functions()
        self.log.info("Jobs is clicked from the drop down successfully")
        job.add()
        self.log.info("Add button is clicked")
        job.job_title(title)
        self.log.info("Job title is typed in the appropriate text box")
        job.click_save()
        self.log.info("Save button is clicked") 
        assert job.assert_job()
        self.log.info("Successfully Saved message is seen and verified")

    @pytest.mark.smoke
    def test_delete_job(self):
        
        """This test case checks the workflow of logging into the application, navigating to the job section,
        deleting a job, and verifying that the job is successfully deleted."""

        job = JobPage(self.driver)
        job.valid_login()
        self.log.info("Successfully logged into the application")
        job.job_functions()
        self.log.info("Jobs is clicked from the drop down successfully")
        job.job_delete()
        self.log.info("Delete button is clicked") 
        job.assert_delete()
        self.log.info("Successfully Deleted message is seen and verified")
