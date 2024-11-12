from config.selenium_config import get_driver, visible_click
from scraper.scraper import scrape_page  
from selenium.webdriver.common.by import By 

def handle_pagination(url, config, browser_name="chrome"):
    """Realiza a navegação entre páginas e coleta os dados."""
    data = []
    next_button_selector = config.get("pagination", {}).get("next_button_selector", None)
    enabled = config.get("pagination", {}).get("enabled", False)

    # Obter o driver do navegador
    driver = get_driver(browser_name)

    while enabled:
        page_data = scrape_page(url, config, browser_name)  # Chamando scrape_page corretamente
        if page_data:
            data.append(page_data)
        
        # Implementar a lógica para clicar no próximo botão de página
        if next_button_selector:
            try:
                visible_click(driver, By.CSS_SELECTOR, next_button_selector)
                
            except Exception as e:
                print(f"Erro ao clicar no botão de próxima página: {e}")
                break

        break  # Remover o `break` se quiser continuar com a navegação

    driver.quit()  # Fechar o navegador após o scraping
    return data
