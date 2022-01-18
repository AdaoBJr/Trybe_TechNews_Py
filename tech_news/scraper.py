import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    if html_content == "":
        return []
    seletor = Selector(html_content)
    card_title = seletor.css("h3 .tec--card__title__link::attr(href)").getall()
    return card_title


# Requisito 3
def scrape_next_page_link(html_content):
    seletor = Selector(html_content)
    next_page = seletor.css(
        "div.tec--list--lg a.tec--btn--lg::attr(href)"
    ).get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
