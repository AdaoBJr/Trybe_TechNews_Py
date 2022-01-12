from parsel import Selector
import requests
import time
from tech_news.helpers import dictTechNews

# source
# https://newbedev.com/try-except-when-using-python-requests-module
# https://www.youtube.com/watch?v=vmRfO2uULfw&ab_channel=pythonbrasil
# https://www.w3schools.com/python/ref_string_strip.asp
# https://parsel.readthedocs.io/en/latest/usage.html
# https://stackoverflow.com/questions/5453422/get-text-in-xpath


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
    selector = Selector(text=html_content)
    next_page = selector.css(".tec--btn::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    news_info = dictTechNews(html_content)
    return news_info


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

