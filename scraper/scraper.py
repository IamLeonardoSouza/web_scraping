import requests
from bs4 import BeautifulSoup

# Função para coletar dados de uma página
def scrape_page(url, config):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Erro ao acessar a página: {url}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    data = {}

    for key, value in config["data_selectors"].items():
        selector = soup.select(value["selector"])
        if value["type"] == "text":
            data[key] = selector[0].get_text() if selector else None
        elif value["type"] == "attribute" and "attribute" in value:
            data[key] = selector[0].get(value["attribute"]) if selector else None

    return data
