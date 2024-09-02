import pytest
from selenium import webdriver

# Fixture for initializing the WebDriver
@pytest.fixture(params=["chrome", "edge"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "edge":
        web_driver = webdriver.Edge()
    request.cls.driver = web_driver
    yield
    web_driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

# Fixture for retrieving the browser option specified in command-line arguments.
@pytest.fixture(scope='class', autouse=True)
def browser(request):
    return request.config.getoption("--browser")



