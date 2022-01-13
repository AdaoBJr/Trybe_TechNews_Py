import requests
import time
from parsel import Selector
from tech_news.functions import (
    get_url,
    get_title,
    get_timestamps,
    get_writer,
    get_shares_count,
    get_comments_count,
    get_summary,
    get_sources,
    get_categories
)


# Requisito 1
def fetch(url):

    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("div.tec--card__info h3 a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("a.tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = get_url(selector)
    title = get_title(selector)
    timestamp = get_timestamps(selector)
    writer = get_writer(selector)
    shares_count = get_shares_count(selector)
    comments_count = get_comments_count(selector)
    summary = get_summary(selector)
    sources = get_sources(selector)
    categories = get_categories(selector)

    news = {}
    news['url'] = url
    news['title'] = title
    news['timestamp'] = timestamp
    # Source https://pt.stackoverflow.com/questions/161505/em-python-existe
    # -opera%C3%A7%C3%A3o-tern%C3%A1ria
    news['writer'] = writer.strip() if writer is not None else None
    news['shares_count'] = shares_count
    news['comments_count'] = int(comments_count)
    news['summary'] = summary
    news['sources'] = sources
    news['categories'] = categories
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
