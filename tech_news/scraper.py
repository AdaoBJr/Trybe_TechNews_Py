import requests
import time
from parsel import Selector


# Requisito 1


def fetch(url):

    try:
        time.sleep(1)
        page = requests.get(url, timeout=3)

        if page.status_code == 200:
            return page.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links = selector.css(
        "div.tec--card__info h3 a::attr(href)"
    ).getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    page = Selector(text=html_content).css(".tec--list > a::attr(href)").get()
    if page:
        return page
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
