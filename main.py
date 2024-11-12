from scraper.config_loader import load_config
from scraper.pagination_handler import handle_pagination

def main():
    config = load_config()
    base_url = config["base_url"]
    data = handle_pagination(base_url, config)
    print(data)

if __name__ == "__main__":
    main()
