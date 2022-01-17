# Requisito 1
import time
import requests
from parsel import Selector


def fetch(url):
    time.sleep(1)

    try:
        res = requests.get(url, timeout=3)
        res.raise_for_status()

    except requests.Timeout:
        return None
    except requests.HTTPError:
        return None

    return res.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    res = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        "div.tec--list.tec--list--lg  article > div > h3 > a::attr(href)"
    )
    return res.getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
