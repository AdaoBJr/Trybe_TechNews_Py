import requests
import time
from parsel import Selector


# Requisito 1
# https://softbranchdevelopers.com/python-requests-library-exception-handling-advanced-request-get-parameters/#all-exceptions
def fetch(url):
    time.sleep(1)
    try:
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

    return selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)

    return selector.css(".tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
