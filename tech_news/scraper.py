import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content) 
    news_list = selector.css('.tec--list--lg h3.tec--card__title > a ::attr(href)').getall()
    return news_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content) 
    next_page_link = selector.css('#js-main > div > div > div.z--col.z--w-2-3 > div.tec--list.tec--list--lg > a::attr(href)').get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
