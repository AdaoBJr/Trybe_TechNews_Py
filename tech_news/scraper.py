import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        res = requests.get(url, timeout=3)
    except requests.exceptions.RequestException:
        return None
    else:
        if res.status_code == 200:
            return res.text
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    result = selector.css("div.tec--card__info h3 a::attr(href)").getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    result = selector.css("a.tec--btn::attr(href)").get()
    return result


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
