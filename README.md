# Flexible Web Scraping

This project allows you to perform web scraping in a modular way, configuring data collection from a `config.json` file. You can adapt the selectors to any web page you want.

## How to Use

1. Edit the `config/config.json` file to define the URL and selectors you want to use.
2. Run the script with the command:

```
python main.py

```

3. The data will be saved in an `output.json` or `output.csv` file.

## Customization

- To add new selectors or change settings, simply modify the `config/config.json` file.
- The script supports pagination. If the page you want to scrape has multiple pages, adjust the pagination settings.

## Dependencies

- `requests`
- `beautifulsoup4`
- `selenium`

Install dependencies with the command:

```
pip install -r requirements.txt

```