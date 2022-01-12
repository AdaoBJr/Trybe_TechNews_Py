import requests
import time
import parsel


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        resp = requests.get(url, timeout=3)
        if resp.status_code == 200:
            return resp.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(text=html_content)
    return selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
