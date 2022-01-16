import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()
        return response.text
    except (requests.ReadTimeout, requests.exceptions.HTTPError):
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    list_links = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        + " div.tec--list.tec--list--lg article > div > h3 > a::attr(href)"
    ).getall()
    return list_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        + " div.tec--list.tec--list--lg > a::attr(href)"
    ).get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
