from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    if html_content == "":
        return list()
    else:
        selector = Selector(text=html_content)
        links = selector.css(
            'h3 a::attr(href)').getall()
        return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    if html_content == "":
        return None
    else:
        selector = Selector(html_content)
        next_page_link = selector.css('.tec--list > a::attr(href)').get()
        return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
