import pytest
from Utility import utility_file
from selenium import webdriver

@pytest.fixture()
def setup_and_teardown(request):
    browser = utility_file.get_config("basic info", "browser")
    driver = None
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Provide a correct browser name")
    
    driver.maximize_window()
    url = utility_file.get_config("basic info", "url")
    driver.get(url)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()
