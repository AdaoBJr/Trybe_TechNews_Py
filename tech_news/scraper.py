from parsel import Selector
import requests
import time

# source
# https://newbedev.com/try-except-when-using-python-requests-module
# https://www.youtube.com/watch?v=vmRfO2uULfw&ab_channel=pythonbrasil
# https://www.w3schools.com/python/ref_string_strip.asp
# https://parsel.readthedocs.io/en/latest/usage.html
# https://stackoverflow.com/questions/5453422/get-text-in-xpath


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timout=3)
        response.raise_for_status()
    except requests.exceptions.ReadTimeout:
        return None
    except requests.exceptions.HTTPError:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    newsLink = selector.css(
        ".tec--card__info h3 .tec--card__title__link::attr(href)"
    ).getall()
    return newsLink


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css(".tec--btn::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    link_canonical = selector.xpath(
        "//link[contains(@rel, 'canonical')]"
    ).get()
    url = Selector(text=link_canonical).css("::attr(href)").get()

    title = selector.css("#js-article-title::text").get().strip()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    getWritersByLinks = selector.xpath(
        "//a[contains(@href,'autor')]/text()"
    ).getall()
    writer = None
    for author in getWritersByLinks:
        if author is not None and author != "":
            writer = author.strip()
    getWriterByCss = selector.css(
        ".tec--author__info p:nth-child(1)::text"
    ).get()
    if getWriterByCss is not None:
        writer = getWriterByCss.strip()
    shares_count = selector.css(
        "#js-author-bar .tec--toolbar__item::text"
    ).get()
    if shares_count == "":
        shares_count = 0
    elif shares_count is not None:
        shares_count = int(shares_count.split()[0])
    else:
        shares_count = 0

    comments_count = selector.css("#js-comments-btn::text").get()
    if comments_count == "":
        comments_count = 0
    elif comments_count is not None:
        try:
            comments_count = int(comments_count.split()[0])
        except IndexError:
            comments_count = 0

    getSummary = selector.css(
        ".tec--article__body p:nth-child(1) *::text"
    ).getall()
    summary = "".join(getSummary).strip("\/n")

    getSources = selector.css(
        ".tec--article__body-grid .z--mb-16 a::text"
    ).getall()
    sources = []
    for source in getSources:
        sources.append(source.strip())

    getCategories = selector.css("#js-categories a::text").getall()
    categories = []
    for category in getCategories:
        categories.append(category.strip())

    news_info = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

    return news_info


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


""" Change for push """
