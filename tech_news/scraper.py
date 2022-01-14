import requests
import time
from parsel import Selector
from tech_news.database import create_news
from tech_news.utils.utils import (
    get_categories,
    get_comments_count,
    get_shares_count,
    get_sources,
    get_summary,
    get_timestamp,
    get_title,
    get_url,
    get_writer
)


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    link = selector.css(
        "div.tec--card__info "
        + "h3.tec--card__title "
        + "a.tec--card__title__link::attr(href)"
    ).getall()

    return link


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    url = selector.css("a.tec--btn::attr(href)")

    if len(url) == 0:
        return None

    return url.get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = get_url(selector)
    title = get_title(selector)
    timestamp = get_timestamp(selector)
    writer = get_writer(selector)
    shares_count = get_shares_count(selector)
    comments_count = get_comments_count(selector)
    summary = get_summary(selector)
    sources = get_sources(selector)
    categories = get_categories(selector)

    new_dict = {}

    new_dict["url"] = url
    new_dict["title"] = title
    new_dict["timestamp"] = timestamp
    new_dict["writer"] = writer
    new_dict["shares_count"] = shares_count
    new_dict["comments_count"] = comments_count
    new_dict["summary"] = summary
    new_dict["sources"] = sources
    new_dict["categories"] = categories

    return new_dict


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    all_news = []
    scraping_result = []
    latest_news = []

    fetch_result = fetch(url)
    all_news = scrape_novidades(fetch_result)

    while len(all_news) < amount:
        base_url = url
        new_fetch = fetch(base_url)

        next_page = scrape_next_page_link(new_fetch)
        new_fetch = fetch(next_page)
        news_list = scrape_novidades(new_fetch)

        for news in news_list:
            all_news.append(news)

        base_url = scrape_next_page_link(new_fetch)

    latest_news = all_news[:amount]

    for news in latest_news:
        html_content = fetch(news)
        news_content = scrape_noticia(html_content)

        scraping_result.append(news_content)

    db = create_news(scraping_result)

    return db
