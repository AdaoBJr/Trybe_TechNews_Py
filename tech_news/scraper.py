from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if not response.status_code == 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("h3.tec--card__title > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("div.tec--list > a::attr(href)").get()


#  css selectors for the news scraping
css_dict = {
    "url": "head > link[rel=canonical]::attr(href)",
    "title": "h1.tec--article__header__title::text",
    "timestamp": "div.tec--timestamp__item > time::attr(datetime)",
    "shares_count": "div.tec--toolbar__item::text",
    "comments_count": "#js-comments-btn::attr(data-count)",
    "summary": ".tec--article__body > p:nth-child(1) *::text",
    "sources": "div.z--mb-16 > div > a::text",
    "categories": "a.tec--badge.tec--badge--primary::text",
    "writer": [
        ".tec--timestamp__item.z--font-bold ::text",
        ".tec--author__info__link ::text",
        "div > p.z--m-none.z--truncate.z--font-bold::text",
    ],
}


# helper functions for the news scraping
def get_all_and_strip(selector, param):
    elements = selector.css(param).getall()
    result = []
    for item in elements:
        result.append(item.strip())
    return result


def get_shares_count(selector, param):
    elem = selector.css(param).get()
    if elem is not None:
        return int(elem.strip().split(" ")[0])
    return 0


def get_a_number(selector, param):
    elem = selector.css(param).get()
    return int(elem)


def get_writer(selector):
    #  thanks for the tip, Pedro Henrique Pires ;)
    for param in css_dict["writer"]:
        author = selector.css(param).get()
        if author is not None:
            return author.strip()
    return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news = {}

    news["url"] = selector.css(css_dict["url"]).get().strip()
    news["title"] = selector.css(css_dict["title"]).get()
    news["timestamp"] = selector.css(css_dict["timestamp"]).get()
    news["writer"] = get_writer(selector)
    news["shares_count"] = get_shares_count(selector, css_dict["shares_count"])
    news["comments_count"] = get_a_number(selector, css_dict["comments_count"])
    news["summary"] = "".join(selector.css(css_dict["summary"]).getall())
    news["sources"] = get_all_and_strip(selector, css_dict["sources"])
    news["categories"] = get_all_and_strip(selector, css_dict["categories"])

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
