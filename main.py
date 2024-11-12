from scraper.config_loader import load_config
from scraper.pagination_handler import handle_pagination
from loguru import logger


def main() -> None:
    """
    Main function to load configuration, set browser, and handle pagination.

    This function:
        - Loads the configuration using `load_config()`.
        - Retrieves the base URL from the configuration.
        - Specifies the browser to be used for web scraping.
        - Handles pagination using `handle_pagination()` and prints the data.

    Returns:
        None
    """
    logger.info("Starting the scraping process.")
    
    config = load_config()
    base_url = config["base_url"]
    
    # Choose browser: "chrome", "firefox", "opera"
    browser_name = "chrome"
    
    data = handle_pagination(base_url, config, browser_name)
    print(data)

if __name__ == "__main__":
    main()
