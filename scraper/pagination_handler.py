from scraper import scrape_page

# Função para navegar entre páginas, se necessário
def handle_pagination(url, config):
    data = []
    next_button_selector = config.get("pagination", {}).get(
        "next_button_selector", None
    )
    enabled = config.get("pagination", {}).get("enabled", False)

    while enabled:
        page_data = scrape_page(url, config)
        if page_data:
            data.append(page_data)
        # Aqui você deveria implementar a lógica para capturar o próximo botão e seguir o link.
        break  # Como exemplo, o loop é interrompido após uma página (remova este break conforme necessário)

    return data
