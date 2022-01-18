import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        res = requests.get(url, timeout=3)
        if res.status_code != 200:
            return None
        else:
            return res.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    links = (
        Selector(text=html_content)
        .css("h3.tec--card__title > a::attr(href)")
        .getall()
    )
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    next = Selector(text=html_content).css(".tec--list > a::attr(href)").get()
    if next:
        return next
    else:
        return None


# Requisito 4
# https://github.com/tryber/sd-010-b-tech-news/pull/47/files
def scrape_noticia(html_content):
    url = (
        Selector(text=html_content)
        .css("link[rel=canonical]::attr(href)")
        .get()
    )

    title = Selector(text=html_content).css("#js-article-title ::text").get()

    timestamp = (
        Selector(text=html_content)
        .css("#js-article-date ::attr(datetime)")
        .get()
    )

    try:
        writer = (
            Selector(text=html_content)
            .css(".z--font-bold")
            .css("*::text")
            .get()
            .strip()
            or ""
        )
    except AttributeError:
        writer = None

    try:
        shares_count = (
            Selector(text=html_content)
            .css(".tec--toolbar__item::text")
            .get()
            .strip()
            .split(" ")[0]
        )
    except AttributeError:
        shares_count = 0

    comments_count = (
        Selector(text=html_content).css(".tec--btn::attr(data-count)").get()
    )

    summary = "".join(
        Selector(text=html_content)
        .css(".tec--article__body > p:first-child *::text")
        .getall()
    )

    sources = (
        Selector(text=html_content).css(".z--mb-16 .tec--badge::text").getall()
    )

    categories = (
        Selector(text=html_content).css(".tec--badge--primary::text").getall()
    )

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
