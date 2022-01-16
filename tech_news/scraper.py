import requests
import time
import re
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        res = requests.get(url, timeout=1)
        res.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    else:
        return res.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css(".tec--list--lg h3 a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".tec--list--lg > a::attr(href)").get()


# Requisito 4 functions
def writer(selector):
    writer = selector.css("a.tec--author__info__link::text").get()
    if writer is None:
        writer = selector.css(
            "div.tec--timestamp div:nth-child(2) a::text"
            ).get()
        if writer is None:
            writer = selector.css("p.z--m-none::text").get()
    return writer.strip()


def share_counter(selector):
    counter = selector.css("div.tec--toolbar__item::text").get()
    if counter:
        counter = int(re.findall(r'\d+', counter)[0])
    else:
        counter = 0
    return counter


def comments_counter(selector):
    return int(selector.css(
        "button#js-comments-btn::attr(data-count)").get())


def summary(selector):
    summary = selector.css(
        "div.tec--article__body > p:nth-child(1) *::text").getall()
    return ''.join(summary)


def sources(selector):
    sources = selector.css("div.z--mb-16 div a::text").getall()
    return [index.strip() for index in sources]


def categories(selector):
    categories = selector.css("div#js-categories a::text").getall()
    return [index.strip() for index in categories]


def url(selector):
    return selector.css("link[rel=canonical]::attr(href)").get()


def title(selector):
    return selector.css("h1.tec--article__header__title::text").get()


def timestamps(selector):
    return selector.css(
        "div.tec--timestamp__item time::attr(datetime)"
        ).get()


# Requisito 4
# Recebi a ajuda de Leticia Galvão, Christian Bugs e Jonathan Souza
def scrape_noticia(html_content):
    selector = Selector(html_content)
    scrape = {
        "url": url(selector),
        "title": title(selector),
        "timestamp": timestamps(selector),
        "writer": writer(selector),
        "shares_count": share_counter(selector),
        "comments_count": comments_counter(selector),
        "summary": summary(selector),
        "sources": sources(selector),
        "categories": categories(selector)
        }
    return scrape


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
