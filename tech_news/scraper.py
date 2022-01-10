import requests
from parsel import Selector
from time import sleep
from tech_news.Tecmundo_scraper import Scrap_tecmundo
from tech_news.database import create_news


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


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    scraped_news = Scrap_tecmundo(selector)
    return scraped_news.mount()


# header Notícias have more hidden news with class .tec--card__title__link, so
#  use id #js-main to restrict to only main news
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    fresh_news = selector.css(
        "#js-main .tec--card__title__link::attr(href)"
    ).getall()
    return fresh_news


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("#js-main .tec--btn::attr(href)").get()
    return next_page


def add_news_to_database(requested_news):
    news_to_insert = []
    for url in requested_news:
        html_content = fetch(url)
        new = scrape_noticia(html_content)
        news_to_insert.append(new)
    create_news(news_to_insert)
    return news_to_insert


def get_tech_news(amount):
    pagination = ""
    base_url = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(base_url + pagination)
    latest_news = scrape_novidades(html_content)

    while len(latest_news) < amount:
        pagination = (scrape_next_page_link(html_content)).split("/novidades")[
            1
        ]
        html_content = fetch(base_url + pagination)
        latest_news.extend(scrape_novidades(html_content))
    requested_news = latest_news[:amount]
    return add_news_to_database(requested_news)
