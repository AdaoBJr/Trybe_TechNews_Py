import requests
import time
from parsel import Selector


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
    selector = Selector(text=html_content.text)
    lis = selector.css(
        ".tec--list--lg h3.tec--card__title a::attr(href)"
        ).getall()
    return lis
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    response = requests.get(html_content)
    selector = Selector(text=response.text)
    link = selector.css(".tec--btn a::attr(href)").get()
    if not link:
        return None
    return link
    """Seu código deve vir aqui"""


def write(selector):
    classes = [
        ".tec--timestamp__item.z--font-bold ::text",
        ".tec--author__info__link ::text",
        "div > p.z--m-none.z--truncate.z--font-bold::text",
    ]
    for item in classes:
        selected_class = selector.css(item).get()
        if selected_class is not None:
            return selected_class.strip()
    return None


def shares_count(selector):
    shares_count = selector.css(".tec--toolbar > div:nth-child(1)::text").get()
    if shares_count is not None:
        result = shares_count.strip().split(" ")[0]
        return int(result)
    return 0


def sources(selector):
    classes = [
        ".z--mb-16 > div > a ::text",
        ".z--mb-16.z--px-16 > div ::text",
    ]
    for item in classes:
        sources = selector.css(item).getall()
        if sources is not []:
            remove_spaces = list(map(lambda x: x.strip(), sources))
            return list(filter(lambda x: x != "", remove_spaces))
    return None


def categories(selector):
    categ = selector.css("#js-categories ::text").getall()
    remove_spaces = list(map(lambda x: x.strip(), categ))
    return list(filter(lambda x: x != "", remove_spaces))


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    obj = {}
    obj["url"] = selector.css("head > link[rel=canonical] ::attr(href)").get()
    obj["title"] = selector.css("#js-article-title ::text").get()
    obj["timestamp"] = selector.css("#js-article-date ::attr(datetime)").get()
    obj["writer"] = write(selector)
    obj["shares_count"] = shares_count(selector)
    obj["comments_count"] = int(
        selector.css("#js-comments-btn ::attr(data-count)").get()
    )
    obj["summary"] = "".join(
        selector.css(".tec--article__body > p:nth-child(1) *::text").getall()
    )
    obj["sources"] = sources(selector)
    obj["categories"] = categories(selector)
    return obj
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
