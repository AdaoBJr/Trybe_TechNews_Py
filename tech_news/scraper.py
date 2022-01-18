import requests
import time

from parsel import Selector

# Requisito 1


def fetch(url):

    try:
        time.sleep(1)
        page_request = requests.get(url, timeout=3)

        if page_request.status_code == 200:
            return page_request.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    all_news_links = selector.css(
        "div.tec--card__info h3 a::attr(href)"
    ).getall()
    return all_news_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
