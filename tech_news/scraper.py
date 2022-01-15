import time
from requests import get
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    STATUS_OK = 200
    try:
        response = get(url, headers={"Accept": "text/html"}, timeout=3)
        return response.text if response.status_code == STATUS_OK else None
    except Exception:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("h3.tec--card__title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".tec--btn--primary::attr(href)").get() or None


# Requisito 4
def get_url(selector):
    return selector.css("head link[rel=canonical]::attr(href)").get()


def scrape_noticia(html_content):
    selector = Selector(html_content)

    return {
        "url": get_url(selector),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
