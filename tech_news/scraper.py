from parsel import Selector
import time
import requests


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None

    if(response.status_code == 200):
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    notice = selector.css("div.tec--list")
    links = notice.css("figure a.tec--card__thumb__link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
