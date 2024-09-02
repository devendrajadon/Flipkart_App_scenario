import pytest

# Base test class that sets up and tears down the WebDriver instance
@pytest.mark.usefixtures("init_driver")
class BaseTest():
    """
    Base test class for setting up and tearing down the WebDriver instance.
    The class uses the 'init_driver' fixture to initialize the WebDriver
    before each test method and perform cleanup after the test method.
    """
    pass