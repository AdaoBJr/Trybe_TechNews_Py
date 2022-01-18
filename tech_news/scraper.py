# Requisito 1
import requests
import time
from parsel import Selector


def fetch(url):
    """Seu código deve vir aqui"""
    try:

        response = requests.get(
            url, timeout=1
        )
        response.raise_for_status()
        return response.text
    except (requests.ReadTimeout, requests.exceptions.HTTPError):
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    links = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        + "div.tec--list.tec--list--lg article > div > h3 > a::attr(href)"
        ).getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
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
