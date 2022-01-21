import requests
import time
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        data = requests.get(url)
        data.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    else:
        return data.text


# Requisito 2
def scrape_novidades(html_content):
    element = Selector(html_content)

    return element.css("div.tec--card__info > h3 > a ::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
