import pytest
from pynput.keyboard import Controller, Key
from Pages.BuzzPage import BuzzPage
from Utility import console_logger

@pytest.mark.usefixtures("setup_and_teardown")
class TestBuzz:
    """TestBuzz class contains test methods to add a post on the buzz page."""
    
    log = console_logger.get_logger()

    @pytest.mark.smoke
    def test_buzz(self):
        """This test case checks the workflow of logging into the application, clicking the buzz,
        and verifying that the post is shared."""
    
        buzz_page = BuzzPage(self.driver)
        self.log.info("BuzzPage object created")
        buzz_page.valid_login()
        self.log.info("Logged in successfully")
        buzz_page.buzz()
        self.log.info("Navigated to buzz page successfully")
        keyboard = Controller()
        keyboard.type("E:\gitpytest_clonemoon.jpeg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        buzz_page.share()
        self.log.info("Post shared")
        buzz_page.assert_saved_message_displayed()
        self.log.info("Post verified successfully")
