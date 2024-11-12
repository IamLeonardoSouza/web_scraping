from config.selenium_config import get_driver

def get_driver_instance(browser_name="chrome"):
    """Retorna o driver configurado para o navegador especificado."""
    return get_driver(browser_name)
