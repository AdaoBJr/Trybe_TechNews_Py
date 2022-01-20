import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.exceptions.HTTPError:  # source: shorturl.at/lsEX6
        return None
    except requests.exceptions.Timeout:
        return None

    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selection = Selector(html_content)
    urls = selection.css('h3.tec--card__title a::attr(href)').getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
