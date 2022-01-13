import requests
import time
from parsel import Selector


# Requisito 1:
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_url = selector.css(
        ".tec--list__item .tec--card__thumb__link::attr(href)"
    ).getall()
    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    news_url = selector.css(".tec--btn::attr(href)").get()
    return news_url


# Requisito 4
def scrape_noticia(html_content):
    try:
        selector = Selector(text=html_content)
        # Referência:
        # https://stackoverflow.com/questions/52849274/getting-the-current-url-page-ref-scrapy
        url = selector.css("link[rel='canonical']::attr(href)").get()
        title = selector.css(".tec--article__header__title::text").get()
        timestamp = selector.css("#js-article-date::attr(datetime)").get()
        writer = selector.css(".z--font-bold *::text").get().strip()
        comments_count = selector.css(".tec--btn::attr(data-count)").get()
        shares_count = (
            selector.css(".tec--toolbar__item::text")
            .get()
            .lstrip()
            .split()[:2][0]
        )
        # Referência:
        # https://www.geeksforgeeks.org/python-string-join-method/

    except AttributeError:
        shares_count = 0

    summary = "".join(
        selector.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )

    sources = selector.css(".z--mb-16 .tec--badge::text").getall()

    categories = selector.css("#js-categories > a::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": [s.strip() for s in sources],
        "categories": [c.strip() for c in categories],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
