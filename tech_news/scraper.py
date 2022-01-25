import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        request = requests.get(url, timeout=5)
        if request.status_code == 200:
            return request.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    novidades = (
        selector.css('''
            .tec--list__item.tec--card__title__link::attr(href)''').getall())
    return novidades


# Requisito 3
def scrape_next_page_link(html_content):
    site_selector = Selector(text=html_content)
    next_page_link = (
        site_selector.css('a.tec--btn::attr(href)').get())
    print(next_page_link)
    if next_page_link == '':
        return None
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
