import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.text
    except requests.HTTPError:
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    response = selector.css(
        ".tec--list--lg .tec--card__title > a ::attr(href)"
    ).getall()
    return response


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    response = selector.css("div.tec--list.tec--list--lg "
                            "> a ::attr(href)").get()
    return response


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("head > link[rel=canonica] ::attr(href)").get()
    title = selector.css("").get()
    timestamp = selector.css("").get()
    writer = selector.css("").get()
    shares_count = selector.css("").get()
    comments_count = selector.css("").get()
    summary = selector.css("").get()
    sources = selector.css("").getall()
    categories = selector.css("").getall()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
