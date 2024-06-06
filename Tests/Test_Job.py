import pytest
from Pages.JobPage import JobPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestJob:
    #@pytest.mark.valid
    def test_add_job(self):
        job = JobPage(self.driver)
        title = utility_file.get_config("valid job details","job_title")
        desc = utility_file.get_config("valid job details","job_descr")
        note = utility_file.get_config("valid job details","job_note")
        job.valid_login()
        job.job_functions()
        job.add()
        job.job_title(title)
        job.job_description(desc)
        job.job_note(note)
        job.click_save()
        assert job.assert_job()

    @pytest.mark.valid
    def test_cancel(self):
        job = JobPage(self.driver)
        title = utility_file.get_config("valid job details","job_title")
        desc = utility_file.get_config("valid job details","job_descr")
        note = utility_file.get_config("valid job details","job_note")
        job.valid_login()
        job.job_functions()
        job.add()
        job.job_title(title)
        job.job_description(desc)
        job.job_note(note)
        job.click_cancel()
        assert job.assert_previous()

    @pytest.mark.valid
    def test_partial_job(self):
        job = JobPage(self.driver)
        title = utility_file.get_config("partial job details","job_title")
        job.valid_login()
        job.job_functions()
        job.add()
        job.job_title(title)
        job.click_save()
        assert job.assert_job()

    def test_delete_job(self):
        job = JobPage(self.driver)
        job.valid_login()
        job.job_functions()
        job.job_delete()
        job.assert_delete()