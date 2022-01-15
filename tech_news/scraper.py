from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        resp = requests.get(url, timeout=3)
        resp.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    else:
        if (resp.status_code == 200):
            return resp.text


# Requisito 2
def scrape_novidades(html_content):
    selectorCss = Selector(text=html_content)
    listLinks = selectorCss.css(
        '.tec--card__info h3 .tec--card__title__link::attr(href)'
    ).getall()

    return listLinks


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
