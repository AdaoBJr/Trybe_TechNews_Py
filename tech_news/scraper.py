import requests
import time
from parsel import Selector
# Requisito 1 - Iniciando o Projeto Tech News


def fetch(url):
    try:
        res = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.Timeout:
        return None
    if res.status_code == 200:
        return res.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    url_news = selector.css("div > h3 > a ::attr(href)").getall()
    return url_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    btn_next_page = selector.css("a.tec--btn--primary ::attr(href)").get()
    if btn_next_page:
        return btn_next_page
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
