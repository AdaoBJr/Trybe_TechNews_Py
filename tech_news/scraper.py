import requests
from parsel import Selector
import re
import time
from requests.exceptions import ReadTimeout
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        request = requests.get(url, timeout=3)
        if request.status_code != 200:
            return None
        return request.text
    except ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    if html_content == "":
        return []
    seletor = Selector(html_content).css(
        'h3 .tec--card__title__link::attr(href)').getall()
    return seletor


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content).css(
        'div.tec--list.tec--list--lg > a ::attr(href)').get()
    return selector


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
    """Seu código deve vir aqui"""
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
    html_content = fetch('https://www.tecmundo.com.br/novidades')
    new_url = scrape_novidades(html_content)
    list_news = []
    while len(new_url) < amount:
        url = scrape_next_page_link(html_content)
        html_content = fetch(url)
        new_url.extend(scrape_novidades(html_content))

    for i in range(amount):
        url_notice = fetch(new_url[i])
        notice_info = scrape_noticia(url_notice)
        list_news += [notice_info]

    create_news(list_news)
    return list_news
