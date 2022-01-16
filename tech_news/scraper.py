import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    try:
        # recurso demora muito a responder
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            pass
    except requests.ReadTimeout:
        # Retornar none
        pass


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    noticias = selector.css(
        ".tec--list__item > article > div > h3 > a::attr(href)"
    ).getall()
    return noticias


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
