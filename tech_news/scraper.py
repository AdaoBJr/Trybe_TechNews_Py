from parsel import Selector
import requests
import time


# source --> https://newbedev.com/try-except-when-using-python-requests-module

# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timout=3)
        response.raise_for_status()
    except requests.exceptions.ReadTimeout:
        return None
    except requests.exceptions.HTTPError:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    newsLink = selector.css(
        ".tec--card__info h3 .tec--card__title__link::attr(href)"
    ).getall()
    return newsLink


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


""" Change for push """
