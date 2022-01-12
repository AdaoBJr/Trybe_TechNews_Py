# Requisito 1
import requests
import time
from parsel import Selector


def fetch(url):
    time.sleep(1)
    try:
        if requests.get(url, timeout=3).status_code == 200:
            get_url = requests.get(url, timeout=3)
            html_content = get_url.text
            return html_content
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links = selector.css(".tec--list--lg .tec--card__title > a ::attr(href)")
    link_notices = links.getall()
    return link_notices


# Requisito 3
def scrape_next_page_link(html_content):
    if html_content == '':
        return None
    else:
        sel = Selector(html_content)
        next_pg = sel.css(".tec--list--lg  .tec--btn--primary::attr(href)")
        return next_pg.get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
