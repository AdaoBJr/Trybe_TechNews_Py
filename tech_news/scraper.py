from operator import indexOf
import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    else:
        if response.status_code != 200:
            return None
        return response.text


def scrape_novidades(html_content):
    selector = Selector(html_content)
    result = selector.css(
        ".tec--list__item .tec--card__title__link ::attr(href)"
    ).getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    result = selector.css(
        ".tec--btn ::attr(href)"
    ).get()
    return result


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    result = {}

    # Souce to get the URL: https://parsel.readthedocs.io/en/latest/usage.html
    result["url"] = selector.css('link[rel*=canonical]::attr(href)').get()
    result["title"] = selector.css(
        '.tec--article__header__title::text').get().strip()
    result["timestamp"] = selector.css(
        '#js-article-date::attr(datetime)'
        ).get()

    # Souce: took Writer this selection from Mari Mohr's PR
    result["writer"] = selector.css(
        ".z--font-bold").css("*::text").get().strip() or " "

    # Source to get int in string:
    # https://stackoverflow.com/questions/11339210/how-to-get-integer-values-from-a-string-in-python

    try:
        shares = selector.css(
            '.tec--toolbar__item::text'
            ).get().strip()
        result["shares_count"] = int(''.join(x for x in shares if x.isdigit()))
    except AttributeError:
        result["shares_count"] = 0

    comments_selector = selector.css(
        '#js-comments-btn::attr(data-count)'
        ).get()
    result["comments_count"] = int(comments_selector)

    result["summary"] = "".join(selector.css(
       ".tec--article__body > p:nth-child(1) ::text"
    ).getall())

    source_selector = selector.css(
        'div.tec--article__body-grid > div.z--mb-16 > div > a::text'
        ).getall()
    result["sources"] = [source.strip() for source in source_selector]
    categories_slector = selector.css(
        '#js-categories > a::text'
        ).getall()
    result["categories"] = [source.strip() for source in categories_slector]
    return result


# Requisito 5
def get_tech_news(amount):
    url_content = fetch("https://www.tecmundo.com.br/novidades")
    latest_news = scrape_novidades(url_content)
    news_by_amount = []

    while len(latest_news) < amount:
        next_page_url = scrape_next_page_link(url_content)
        new_news = fetch(next_page_url)
        latest_news.extend(scrape_novidades(new_news))
        print(latest_news)

    for news in latest_news:
        if indexOf(latest_news, news) < amount:
            news_to_fetch = fetch(news)
            news_scrapper = scrape_noticia(news_to_fetch)
            news_by_amount.append(news_scrapper)

    create_news(news_by_amount)
    return news_by_amount
