from config.selenium_config import get_driver, visible_keys
from selenium.webdriver.common.by import By 

def scrape_page(url, config, browser_name="chrome"):
    """Realiza o scraping de uma página usando o navegador configurado."""
    # Obter o driver do navegador
    driver = get_driver(browser_name)
    
    driver.get(url)
    
    data = {}

    for key, value in config["data_selectors"].items():
        elements = driver.find_elements(By.CSS_SELECTOR, value["selector"])  # Usando By corretamente
        if value["type"] == "text":
            data[key] = elements[0].text if elements else None
        elif value["type"] == "attribute" and "attribute" in value:
            data[key] = elements[0].get_attribute(value["attribute"]) if elements else None

    driver.quit()  # Fechar o navegador após o scraping
    return data
