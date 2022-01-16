
import time
import requests
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
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    return Selector(text=html_content).css("h3 > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    return Selector(text=html_content).css(
        "div.tec--list a.tec--btn::attr(href)"
        ).get()


# ---------- HELPERS ---------- #

def get_writer(selector):
    options = [
        "div > p.z--m-none.z--truncate.z--font-bold::text",
        ".tec--author__info__link ::text",
        "div.tec--timestamp div:nth-child(2) a::text",
    ]

    for val in options:
        target = selector.css(val).get()
        if target:
            return target.strip()


def get_shares_count(selector):
    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count:
        return int((shares_count.strip()).split(" ")[0])
    else:
        return 0

# ---------- HELPERS ---------- #


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    writer = get_writer(selector)
    shares_count = get_shares_count(selector)

    return {
        "url": selector.css("meta[property='og:url']::attr(content)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": int(selector.css(
            "button.tec--btn::attr(data-count)"
            ).get()),
        "summary": "".join(selector.css(
             ".tec--article__body > p:first-child *::text").getall()),
        "sources": [source.strip() for source in selector.css(
            ".z--mb-16 div a.tec--badge::text").getall()],
        "categories": [category.strip() for category in selector.css(
                "#js-categories .tec--badge::text").getall()],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
