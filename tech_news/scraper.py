import requests
import time
from parsel import Selector


# Requisito 1:
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_url = selector.css(
        ".tec--list__item .tec--card__thumb__link::attr(href)"
    ).getall()
    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    news_url = selector.css(".tec--btn::attr(href)").get()
    return news_url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
