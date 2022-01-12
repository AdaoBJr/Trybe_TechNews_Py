import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    css_selector = '.tec--list--lg h3.tec--card__title > a ::attr(href)'
    news_list = selector.css(css_selector).getall()
    return news_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(
        '#js-main > div > div > div.z--col.z--w-2-3 > '
        'div.tec--list.tec--list--lg > a ::attr(href)'
    ).get()
    return None if not next_page_link else next_page_link


# Requisito 4
def format_writter(writter):
    if writter is not None:
        return writter.strip()
    else:
        return None


def format_shares(shares_text):
    if shares_text is not None:
        trimmed_str = shares_text.strip()
        str_number = trimmed_str.split(' ')[0]
        shares_count = int(str_number)
        return shares_count
    else:
        return 0


def format_comments(text):
    return int(text)


def trim_list(list):
    formated_list = []
    for item in list:
        formated_list.append(item.strip())
    return formated_list


def get_categories(selector):
    return trim_list(
        selector.css(
            '#js-categories a::text'
        ).getall()
    )


def get_sources(selector):
    return trim_list(
        selector.css(
            '.z--mb-16 > div > a::text'
        ).getall()
    )


def get_summary(selector):
    return ''.join(
        selector.css(
            '.tec--article__body > p:nth-child(1) *::text'
        ).getall()
    )


def get_comments(selector):
    return format_comments(
        selector.css(
            '#js-comments-btn::attr(data-count)'
        ).get()
    )


def get_shares(selector):
    return format_shares(
        selector.css(
            '#js-author-bar > nav > div:nth-child(1)::text'
        ).get()
    )


def get_writter(selector):
    # Portella foi uma boa ajuda <3
    # https://github.com/tryber/sd-010-b-tech-news/blob/ebc0371950681c1b1b1f49a27e10131dd49b847c/tech_news/Tecmundo_scraper.py#L25
    query_selectors = [
        ".tec--author__info__link::text",
        ".tec--timestamp a::text",
        "#js-author-bar > div p::text",
    ]
    for query in query_selectors:
        result = selector.css(query).get()
        if result is not None:
            return result.strip()
    return None


def get_timestamp(selector):
    return selector.css(
        '#js-article-date::attr(datetime)'
    ).get()


def get_title(selector):
    return selector.css(
        '#js-article-title::text'
    ).get()


def get_url(selector):
    return selector.css(
        "head > link[rel=canonical]::attr(href)"
    ).get()


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    return {
        "url": get_url(selector),
        "title": get_title(selector),
        "timestamp": get_timestamp(selector),
        "writer": get_writter(selector),
        "shares_count": get_shares(selector),
        "comments_count": get_comments(selector),
        "summary": get_summary(selector),
        "sources": get_sources(selector),
        "categories": get_categories(selector),
    }


# Requisito 5
def get_tech_news(amount):
    url = 'https://www.tecmundo.com.br/novidades'
    html_content = fetch(url)
    news_urls = scrape_novidades(html_content)
    news_list = []

    while len(news_urls) < amount:
        url = scrape_next_page_link(html_content)
        html_content = fetch(url)
        news_urls.extend(scrape_novidades(html_content))

    for index in range(amount):
        notice_url = news_urls[index]
        notice_page = fetch(notice_url)
        notice_info = scrape_noticia(notice_page)
        news_list.append(notice_info)

    create_news(news_list)
    return news_list
