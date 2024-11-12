from scraper.config_loader import load_config
from scraper.pagination_handler import handle_pagination

def main():
    config = load_config()
    base_url = config["base_url"]
    
    # Escolha o navegador: "chrome", "firefox", "opera"
    browser_name = "chrome"
    
    data = handle_pagination(base_url, config, browser_name)
    print(data)

if __name__ == "__main__":
    main()
