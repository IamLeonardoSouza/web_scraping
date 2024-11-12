from config.selenium_config import get_driver, visible_keys
from selenium.webdriver.common.by import By
from typing import Dict, Any, Optional


def scrape_page(url: str, config: Dict[str, Any], browser_name: str = "chrome") -> Dict[str, Optional[Any]]:
    """
    Scrapes a page using the configured browser.

    Args:
        url (str): The URL of the page to scrape.
        config (Dict[str, Any]): A configuration dictionary containing data selectors.
        browser_name (str, optional): The name of the browser to use ("chrome", "firefox", "opera"). Defaults to "chrome".

    Returns:
        Dict[str, Optional[Any]]: A dictionary with scraped data, where the values are either text or attribute values.
    """
    # Get browser driver
    driver = get_driver(browser_name)
    
    driver.get(url)
    
    data: Dict[str, Optional[Any]] = {}

    for key, value in config["data_selectors"].items():
        elements = driver.find_elements(By.CSS_SELECTOR, value["selector"])  # Using By correctly
        if value["type"] == "text":
            data[key] = elements[0].text if elements else None
        elif value["type"] == "attribute" and "attribute" in value:
            data[key] = elements[0].get_attribute(value["attribute"]) if elements else None

    driver.quit()  # Close browser after scraping
    return data
