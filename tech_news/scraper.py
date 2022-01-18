import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css("h3 .tec--card__title__link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css("a.tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get()
    if not writer:
        writer = None
    else:
        writer = writer.strip()

    shares_count = selector.css(".tec--toolbar__item::text").get()
    if not shares_count:
        shares_count = 0
    else:
        shares_count = int(shares_count.split(" ")[1])

    comments_count = selector.css("button.tec--btn::attr(data-count)").get()
    if not comments_count:
        comments_count = 0
    else:
        comments_count = int(comments_count)
    summary = selector.css(
        "div.tec--article__body > p:first-child *::text").getall()
    sources = selector.css("div.z--mb-16 a::text").getall()
    categories = selector.css("div#js-categories a::text").getall()

    info_news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": "".join(summary),
        "sources": [src.strip() for src in sources],
        "categories": [category.strip() for category in categories]
    }
    return info_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
