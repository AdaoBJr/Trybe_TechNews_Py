import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news = selector.css(
        'div.tec--list .tec--card__thumb__link::attr(href)'
    ).getall()
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css('div.tec--list a.tec--btn::attr(href)').get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
