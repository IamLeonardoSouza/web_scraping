from config.selenium_config import get_driver
from selenium.webdriver.remote.webdriver import WebDriver


def get_driver_instance(browser_name: str = "chrome") -> WebDriver:
    """
    Returns the configured driver for the specified browser.

    Args:
        browser_name (str, optional): The name of the browser to use. Defaults to "chrome".

    Returns:
        WebDriver: An instance of the configured browser's WebDriver.
    """
    return get_driver(browser_name)
