from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Configurações de tempo de espera e outras constantes
DEFAULT_WAIT_TIME = 10

def get_wait(driver: webdriver):
    """Retorna o WebDriverWait configurado com o tempo de espera padrão."""
    return WebDriverWait(driver, DEFAULT_WAIT_TIME)

def visible_click(driver: webdriver, by: By, locator: str):
    """Clica em um elemento que é visível na página."""
    wait = get_wait(driver)
    element = wait.until(EC.element_to_be_clickable((by, locator)))
    element.click()

def visible_keys(driver: webdriver, by: By, locator: str, keys: str):
    """Envia teclas para um campo de texto visível."""
    wait = get_wait(driver)
    element = wait.until(EC.visibility_of_element_located((by, locator)))
    element.send_keys(keys)

def visible_clear(driver: webdriver, By: By, locator: str):
    wait = get_wait(driver)
    element = wait.until(EC.visibility_of_element_located((By, locator)))
    element.clear()

def get_driver(browser_name="chrome"):
    """Retorna o driver do navegador configurado."""
    if browser_name == "chrome":
        return _init_chrome_driver()
    elif browser_name == "firefox":
        return _init_firefox_driver()
    else:
        raise ValueError(f"Navegador {browser_name} não suportado!")

def _init_chrome_driver():
    """Inicia o driver do Chrome com opções configuradas."""
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver_path = "/path/to/chromedriver"
    return webdriver.Chrome(service=ChromeService(driver_path), options=chrome_options)

def _init_firefox_driver():
    """Inicia o driver do Firefox com opções configuradas."""
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver_path = "/path/to/geckodriver"
    return webdriver.Firefox(service=FirefoxService(driver_path), options=firefox_options)

def switch_to_iframe(driver: webdriver, by: By, locator: str):
    """Troca para um iframe especificado."""
    wait = get_wait(driver)
    iframe = wait.until(EC.presence_of_element_located((by, locator)))
    driver.switch_to.frame(iframe)

def switch_to_default_content(driver: webdriver):
    """Volta ao conteúdo padrão da página."""
    driver.switch_to.default_content()

def is_element_present(driver: webdriver, by: By, locator: str) -> bool:
    """Verifica se um elemento está presente na página."""
    try:
        driver.find_element(by, locator)
        return True
    except NoSuchElementException:
        return False
