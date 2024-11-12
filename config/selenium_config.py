from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from typing import Optional


# Waiting time settings and other constants
DEFAULT_WAIT_TIME = 10

def get_wait(driver: webdriver) -> WebDriverWait:
    """
    Returns the WebDriverWait configured with the default wait time.

    Args:
        driver (webdriver): The WebDriver instance for which the wait is configured.

    Returns:
        WebDriverWait: The configured WebDriverWait instance.
    """
    return WebDriverWait(driver, DEFAULT_WAIT_TIME)

def visible_click(driver: webdriver, by: By, locator: str) -> None:
    """
    Clicks on an element that is visible on the page.

    Args:
        driver (webdriver): The WebDriver instance.
        by (By): The method to locate the element.
        locator (str): The locator value to find the element.
    """
    wait = get_wait(driver)
    element = wait.until(EC.element_to_be_clickable((by, locator)))
    element.click()

def visible_keys(driver: webdriver, by: By, locator: str, keys: str) -> None:
    """
    Sends keys to a visible text field.

    Args:
        driver (webdriver): The WebDriver instance.
        by (By): The method to locate the element.
        locator (str): The locator value to find the element.
        keys (str): The text to send to the element.
    """
    wait = get_wait(driver)
    element = wait.until(EC.visibility_of_element_located((by, locator)))
    element.send_keys(keys)

def visible_clear(driver: webdriver, by: By, locator: str) -> None:
    """
    Clears the contents of a visible text field.

    Args:
        driver (webdriver): The WebDriver instance.
        by (By): The method to locate the element.
        locator (str): The locator value to find the element.
    """
    wait = get_wait(driver)
    element = wait.until(EC.visibility_of_element_located((by, locator)))
    element.clear()

def get_driver(browser_name: str = "chrome") -> webdriver:
    """
    Returns the configured browser driver.

    Args:
        browser_name (str, optional): The name of the browser to use ("chrome" or "firefox"). Defaults to "chrome".

    Returns:
        webdriver: The browser's WebDriver instance.
    
    Raises:
        ValueError: If the browser is not supported.
    """
    if browser_name == "chrome":
        return _init_chrome_driver()
    elif browser_name == "firefox":
        return _init_firefox_driver()
    else:
        raise ValueError(f"Browser {browser_name} not supported!")

def _init_chrome_driver() -> webdriver.Chrome:
    """
    Starts Chrome driver with configured options.

    Returns:
        webdriver.Chrome: The Chrome WebDriver instance.
    """
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver_path = "/path/to/chromedriver"
    return webdriver.Chrome(service=ChromeService(driver_path), options=chrome_options)

def _init_firefox_driver() -> webdriver.Firefox:
    """
    Starts Firefox driver with configured options.

    Returns:
        webdriver.Firefox: The Firefox WebDriver instance.
    """
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver_path = "/path/to/geckodriver"
    return webdriver.Firefox(service=FirefoxService(driver_path), options=firefox_options)

def switch_to_iframe(driver: webdriver, by: By, locator: str) -> None:
    """
    Switch to a specified iframe.

    Args:
        driver (webdriver): The WebDriver instance.
        by (By): The method to locate the iframe.
        locator (str): The locator value to find the iframe.
    """
    wait = get_wait(driver)
    iframe = wait.until(EC.presence_of_element_located((by, locator)))
    driver.switch_to.frame(iframe)

def switch_to_default_content(driver: webdriver) -> None:
    """
    Switches to the default page content.

    Args:
        driver (webdriver): The WebDriver instance.
    """
    driver.switch_to.default_content()

def is_element_present(driver: webdriver, by: By, locator: str) -> bool:
    """
    Checks if an element is present on the page.

    Args:
        driver (webdriver): The WebDriver instance.
        by (By): The method to locate the element.
        locator (str): The locator value to find the element.

    Returns:
        bool: True if the element is present, False otherwise.
    """
    try:
        driver.find_element(by, locator)
        return True
    except NoSuchElementException:
        return False
