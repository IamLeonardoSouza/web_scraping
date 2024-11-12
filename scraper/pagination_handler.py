from config.selenium_config import get_driver, visible_click
from scraper.scraper import scrape_page  
from selenium.webdriver.common.by import By
from typing import Dict, Any, List, Optional
from loguru import logger


def handle_pagination(url: str, config: Dict[str, Any], browser_name: str = "chrome") -> List[Dict[str, Optional[Any]]]:
    """
    Performs navigation between pages and collects data.

    Args:
        url (str): The URL of the page to scrape.
        config (Dict[str, Any]): A configuration dictionary containing pagination and data selectors.
        browser_name (str, optional): The name of the browser to use ("chrome", "firefox", "opera"). Defaults to "chrome".

    Returns:
        List[Dict[str, Optional[Any]]]: A list of dictionaries containing the scraped data from each page.
    """
    data: List[Dict[str, Optional[Any]]] = []
    next_button_selector = config.get("pagination", {}).get("next_button_selector", None)
    enabled = config.get("pagination", {}).get("enabled", False)

    # Get browser driver
    driver = get_driver(browser_name)
    logger.info(f"Starting scraping with navigation between pages: {url}")

    while enabled:
        logger.info(f"Collecting page data: {url}")
        page_data = scrape_page(url, config, browser_name)  # Calling scrape_page correctly
        if page_data:
            data.append(page_data)
            logger.info(f"Data collected for the page {url}: {page_data}")
        
        # Implement logic to click the next page button
        if next_button_selector:
            try:
                visible_click(driver, By.CSS_SELECTOR, next_button_selector)
                logger.info(f"Clicking on 'Next Page' button with selector {next_button_selector}")
                
            except Exception as e:
                logger.error(f"Error when clicking next page button: {e}")
                break

        break  # Remove `break` if you want to continue browsing

    driver.quit()  # Close browser after scraping
    logger.info("Navigation finished and browser driver closed.")
    return data
