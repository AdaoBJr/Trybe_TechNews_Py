import time
import re
from requests import get
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    STATUS_OK = 200
    try:
        response = get(url, headers={"Accept": "text/html"}, timeout=3)
        return response.text if response.status_code == STATUS_OK else None
    except Exception:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("h3.tec--card__title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".tec--btn--primary::attr(href)").get() or None


# Requisito 4
def get_url(selector):
    return selector.css("head link[rel=canonical]::attr(href)").get()


def get_title(selector):
    return selector.css(".tec--article__header__title::text").get()


def get_timestamp(selector):
    return selector.css(".tec--timestamp__item time::attr(datetime)").get()


def get_writer(selector):
    selectors = [
        ".tec--timestamp:nth-child(1) a::text",
        ".tec--author__info p:first-child::text",
        ".tec--author__info p:first-child a::text",
    ]
    selected = []
    for curr_selector in selectors:
        selected_writer = selector.css(curr_selector).get()
        if selected_writer is not None:
            selected.append(selected_writer.strip())
        if selected_writer is None:
            selected.append(None)
    writer = [item for item in selected if item]
    if len(writer) == 0:
        return None
    return writer[0]


def get_shares_count(selector):
    shares = selector.css(".tec--toolbar div:first-child::text").get()
    if shares is None or not ("Compartilharam") in shares:
        return 0
    shares_count = re.findall(r"\s(\d*)\s(...*)", shares)
    return int(shares_count[0][0])


def get_comments_count(selector):
    comments = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments is None:
        return 0
    return int(comments)


def get_summary(selector):
    summary_selector = "div.tec--article__body > p:nth-child(1) *::text"
    summary = selector.css(summary_selector).getall()
    return ''.join(summary)


def get_sources(selector):
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    return [item.strip() for item in sources]


def get_categories(selector):
    categories = selector.css("#js-categories a::text").getall()
    return [item.strip() for item in categories]


def scrape_noticia(html_content):
    selector = Selector(html_content)

    return {
        "url": get_url(selector),
        "title": get_title(selector),
        "timestamp": get_timestamp(selector),
        "writer": get_writer(selector),
        "shares_count": get_shares_count(selector),
        "comments_count": get_comments_count(selector),
        "summary": get_summary(selector),
        "sources": get_sources(selector),
        "categories": get_categories(selector),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
