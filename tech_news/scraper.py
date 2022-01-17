import requests
import time
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    if response.status_code == 200:
        return response.text
    else:
        return None


def scrape_novidades(html_content):
    selector = Selector(html_content)
    url_link = 'div h3 a ::attr(href)'
    url_list = selector.css(url_link).getall()
    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
