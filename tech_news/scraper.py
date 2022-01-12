
import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, timeout=3)
        if res.status_code == 200:
            return res.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    css_path = ".tec--list--lg h3.tec--card__title > a ::attr(href)"

    return selector.css(css_path).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    css_path = "div.tec--list--lg > a ::attr(href)"

    return selector.css(css_path).get()


# Requisito 4
# https://www.codegrepper.com/code-examples/python/remove+first+and+last+spaces+in+string+python
def remove_spaces(list):
    new_list = []
    for item in list:
        new_list.append(item.strip())

    return new_list


def get_url(selector):
    return selector.css("head > link[rel=canonical]::attr(href)").get()


def get_title(selector):
    title = selector.css("h1.tec--article__header__title::text").get()
    return title


def get_date(selector):
    css_path = "div.tec--timestamp__item > time ::attr(datetime)"
    return selector.css(css_path).get()


def get_writer(selector):
    # help do Denis
    # https://github.com/tryber/sd-010-b-tech-news/blob/denis-rossati-tech-news/tech_news/scraper.py
    writer_selectors = [
        '//*[@class="tec--timestamp__item z--font-bold"]/a/text()',
        '//a[@class="tec--author__info__link"]/text()',
        '//*[@id="js-author-bar"]/div/p/text()'
    ]

    for path in writer_selectors:
        writer = selector.xpath(path).get()
        if writer is not None:
            return writer.strip()
    return None


# ref: https://devhints.io/xpath#class-check
def get_shares(selector):
    shares = selector.xpath('//*[@id="js-author-bar"]/nav/div[1]/text()').get()
    if shares is None:
        return 0
    result = shares.split()
    return int(result[0])


def get_comments(selector):
    cmts = selector.xpath('//*[@id="js-comments-btn"]/@data-count').get()
    if cmts is None:
        return 0
    return int(cmts)


def get_summary(selector):
    return ''.join(selector.css(
        '.tec--article__body > p:nth-child(1) *::text'
    ).getall())


def get_categories(selector):
    categories = selector.xpath(
        '//*[@id="js-categories"]/a/text()'
    ).getall()

    return remove_spaces(categories)


def get_source(selector):
    source = selector.css(
        # '//*[@class="z--mb-16"]/div/a/text()'
        ".z--mb-16 > div > a::text"
    ).getall()

    return remove_spaces(source)


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    result = {
        "url": get_url(selector),
        "title": get_title(selector),
        "timestamp": get_date(selector),
        "writer": get_writer(selector),
        "shares_count": get_shares(selector),
        "comments_count": get_comments(selector),
        "summary": get_summary(selector),
        "sources": get_source(selector),
        "categories": get_categories(selector)
    }

    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
