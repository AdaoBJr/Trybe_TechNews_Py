import requests
import time
from parsel import Selector
# https://parsel.readthedocs.io/en/latest/usage.html


def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, timeout=3)
        res.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    return res.text


def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    get_html_content = Selector(html_content).xpath(
      "/html/body/div/main/div/div/div/div/div/article/div/h3/a/@href"
    ).getall()
    return get_html_content


def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    get_html_content = Selector(html_content).xpath(
      "/html/body/div/main/div/div/div/div/a/@href"
    ).get()
    return get_html_content


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    news = []
    URL = "https://www.tecmundo.com.br/novidades"
    while len(news) < amount:
        page = fetch(URL)
        links = scrape_novidades(page)
        for link in links:
            fetch_page = fetch(link)
            scrape_page = scrape_noticia(fetch_page)
            if len(news) == amount:
                break
            news.append(scrape_page)
        URL = scrape_next_page_link(page)
    create_news(news)

    return news
