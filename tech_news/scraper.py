import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, timeout=3)
        if not res.status_code == 200:
            return None
        return res.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    result = selector.css(
        ".tec--list--lg .tec--card__title > a ::attr(href)"
    ).getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    result = selector.css(
        ".tec--list.tec--list--lg > a ::attr(href)"
    ).get()
    return result


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
