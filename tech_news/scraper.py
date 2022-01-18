import requests
from time import sleep
from parsel import Selector
import re
from tech_news.database import create_news

GETTER = {
    "news": "#js-main .tec--card__title__link::attr(href)",
    "next": "#js-main .tec--btn::attr(href)",
    "url": "link[rel=canonical]::attr(href)",
    "title": "#js-article-title::text",
    "writer": ".z--font-bold",
    "shares_number": "#js-author-bar div:nth-child(1)::text",
    "comments_number": "#js-comments-btn::attr(data-count)",
    "sumary": "div.tec--article__body p:nth-child(1) *::text",
    "sources": ".z--mb-16 .tec--badge::text",
    "categories": ".tec--badge--primary::text",
    "timestamp": "#js-article-date::attr(datetime)",
}

# BASED ON *
# https://www.w3schools.com/python/ref_requests_get.asp
# https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
# https://github.com/tryber/sd-10b-live-lectures/blob/lecture/34.3/main_scraper.py
# *


# Requisito 1
def fetch(url):
    response = ""
    try:
        sleep(1)
        response = requests.get(url, timeout=3)

    except requests.exceptions.RequestException:
        pass

    finally:
        if response != "" and response.status_code == 200:
            return response.text
        pass


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    news = selector.css(GETTER["news"]).getall()
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    result = selector.css(GETTER["next"]).get()

    return result


# BASED ON *
# https://www.w3schools.com/python/ref_string_strip.asp
# https://docs.python.org/3/library/re.html
# https://www.w3schools.com/python/ref_string_join.asp
# *


# Requisito 4
def scrape_noticia(html_content):
    content = Selector(html_content)
    shares_number = content.css(GETTER["shares_number"]).get() or "0"
    comments_number = content.css(GETTER["comments_number"]).get() or "0"
    return {
        "title": content.css(GETTER["title"]).get(),
        "url": content.css(GETTER["url"]).get(),
        "writer": content.css(".z--font-bold").css("*::text").get().strip()
        or "",
        "shares_count": int(re.sub("[^0-9]", "", shares_number)),
        "comments_count": int(comments_number),
        "summary": "".join(content.css(GETTER["sumary"]).getall()),
        "sources": [text.strip() for text in (
          content.css(GETTER["sources"]).getall())],
        "categories": [text.strip() for text in (
          content.css(GETTER["categories"]).getall())],
        "timestamp": content.css(GETTER["timestamp"]).get(),
    }


# Requisito 5
def get_tech_news(amount):
    fetch_url = fetch("https://www.tecmundo.com.br/novidades")
    news_list = scrape_novidades(fetch_url)
    content = []

    while len(news_list) < amount:
        next_page = fetch(scrape_next_page_link(fetch_url))
        news_list.extend(scrape_novidades(next_page))

    for i in range(amount):
        news_url = news_list[i]
        result = fetch(news_url)
        content.append(scrape_noticia(result))

    create_news(content)
    return content
