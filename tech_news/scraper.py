import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if not response.status_code == 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content.text)
    lis = selector.css(
        ".tec--list--lg h3.tec--card__title a::attr(href)"
        ).getall()
    return lis
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    response = requests.get(html_content)
    selector = Selector(text=response.text)
    link = selector.css(".tec--btn a::attr(href)").get()
    if not link:
        return None
    return link
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
