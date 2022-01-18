import requests
import time
from parsel import Selector
from tech_news.aux_functions import (
    get_news_url,
    get_news_title,
    get_news_timestamp,
    get_news_writer,
    get_news_shares_count,
    get_news_comments_count,
    get_news_summary,
    get_news_sources,
    get_news_categories,
)
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    if response.status_code == 200:
        return response.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    url_link = 'div h3 a ::attr(href)'
    url_list = selector.css(url_link).getall()
    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_button = "a.tec--btn--primary ::attr(href)"
    next_page_link = selector.css(next_page_button).get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news_url = get_news_url(selector)
    news_title = get_news_title(selector)
    news_timestamp = get_news_timestamp(selector)
    writer = get_news_writer(selector)
    news_shares_count = get_news_shares_count(selector)
    news_comments_count = get_news_comments_count(selector)
    news_summary = get_news_summary(selector)
    news_sources = get_news_sources(selector)
    news_categories = get_news_categories(selector)

    news_dict = {}
    news_dict['url'] = news_url
    news_dict['title'] = news_title
    news_dict['timestamp'] = news_timestamp
    news_dict['writer'] = writer.strip() if writer is not None else None
    news_dict['shares_count'] = news_shares_count
    news_dict['comments_count'] = int(news_comments_count)
    news_dict['summary'] = news_summary
    news_dict['sources'] = news_sources
    news_dict['categories'] = news_categories

    return news_dict


# Requisito 5
def get_tech_news(amount):
    destiny_url = fetch('https://www.tecmundo.com.br/novidades')
    new_stuff = scrape_novidades(destiny_url)
    next_page_news = scrape_next_page_link(destiny_url)

    while len(new_stuff) < amount:
        destiny_url = fetch(next_page_news)
        new_stuff.extend(scrape_novidades(destiny_url))

    returned_news = []
    for news in new_stuff[:amount]:
        news_link = fetch(news)
        returned_news.append(scrape_noticia(news_link))

    create_news(returned_news)

    return returned_news
