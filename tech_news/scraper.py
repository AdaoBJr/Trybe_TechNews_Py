import requests
from parsel import Selector
from time import sleep
from tech_news.Tecmundo_scraper import Scrap_tecmundo


# Requisito 1
# https://softbranchdevelopers.com/python-requests-library-exception-handling-advanced-request-get-parameters/#all-exceptions
def fetch(url):
    resp = ""
    try:
        sleep(1)
        resp = requests.get(url, timeout=3)
    except requests.exceptions.RequestException:
        return None
    finally:
        if resp != "" and resp.status_code == 200:
            return resp.text
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    scraped_news = Scrap_tecmundo(selector)
    return scraped_news.mount()


# Requisito 3
# header Notícias have more hidden news with class .tec--card__title__link, so
#  use id #js-main to restrict to only main news
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    fresh_news = selector.css(
        "#js-main .tec--card__title__link::attr(href)"
    ).getall()
    return fresh_news


content = fetch("https://www.tecmundo.com.br/novidades")

print(scrape_novidades(content))

# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
