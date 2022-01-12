import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    return selector.css("article > div > h3 > a ::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    return selector.css("div.tec--list.tec--list--lg > a ::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    url = selector.css("head > link[rel=canonical] ::attr(href)").get()
    title = selector.css("#js-article-title ::text").get()
    timestamp = selector.css("#js-article-date ::attr(datetime)").get()
    try:
        writer = selector.css(".z--font-bold ::text").get().strip()
    except AttributeError:
        writer = ""
    try:
        shares_count = (
            selector.css("#js-author-bar > nav > div:nth-child(1) ::text")
            .get()
            .strip()
            .split(" ")[0]
        )
    except AttributeError:
        shares_count = 0
    comments_count = selector.css("#js-comments-btn ::attr(data-count)").get()
    summary = selector.css(
        "div.tec--article__body-grid >"
        " div.tec--article__body > p:nth-child(1) ::text"
    ).getall()

    sources = selector.css(".z--mb-16 .tec--badge ::text").getall()
    categories = selector.css("#js-categories > a ::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": "".join(summary),
        "sources": [i.strip() for i in sources],
        "categories": [i.strip() for i in categories],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
