import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        r = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    else:
        if r.status_code != 200:
            return None
        return r.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    # agradecimentos ao Gabriel Essênio pela ajuda
    # na compreensão dos seletores na função css
    return selector.css(
        ".tec--list--lg .tec--card__title > a ::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
