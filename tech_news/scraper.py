import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news = selector.css("div.tec--list")
    get_links_of_news = news.css(
        "figure a.tec--card__thumb__link::attr(href)"
    ).getall()
    return get_links_of_news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    html = fetch(url)
    news_list = scrape_novidades(html)
    news_scraped = []

    while len(news_scraped) < amount:
        for link in news_list:
            html = fetch(link)
            if html:
                news = scrape_noticia(html)
                news_scraped.append(news)
                if len(news_scraped) == amount:
                    break
        if scrape_next_page_link(html):
            url = scrape_next_page_link(html)
            html = fetch(url)
            news_list = scrape_novidades(html)
        else:
            break

    create_news(news_scraped)
    return news_scraped
