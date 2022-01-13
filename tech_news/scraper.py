import requests
import time
import parsel


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        result = requests.get(url, timeout=3)
        if result.status_code == 200:
            return result.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    return selector.css("h3.tec--card__title > a ::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    return selector.css("div.tec--list.tec--list--lg > a ::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
