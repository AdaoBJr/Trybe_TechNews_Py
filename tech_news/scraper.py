import requests
from parsel import Selector
import time
from requests.exceptions import ReadTimeout


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        request = requests.get(url, timeout=3)
        if request.status_code != 200:
            return None
        return request.text
    except ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    if html_content == "":
        return []
    seletor = Selector(html_content).css(
        'h3 .tec--card__title__link::attr(href)').getall()
    return seletor


# Requisito 3
def scrape_next_page_link(html_content):
    seletor = Selector(html_content).css(
        "div.tec--list--lg a.tec--btn--lg::attr(href)").get()
    return seletor


# Requisito 4
def scrape_noticia(html_content):
    result = []
    if html_content == "":
        return result
    seletor = Selector(html_content).css(
        '.tec--card__title__link::attr(href)').getall()
    for item in seletor:
        result.append(item)
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


