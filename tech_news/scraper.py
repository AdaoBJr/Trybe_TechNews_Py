import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    return selector.css("h3 > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    return selector.css(".tec--list--lg > a::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    comments = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments is None:
        comments_total = 0
    comments_total = int(comments)
    try:
        share_total = int(
            "".join(
                filter(
                    str.isdigit,
                    selector.css(".tec--toolbar__item::text").getall()[0],
                )
            )
        )
    except IndexError:
        share_total = 0

    return {
        "url": selector.css("head > link[rel=canonical]::attr(href)").get(),
        "title": selector.css('#js-article-title::text').get(),
        "timestamp": selector.css('#js-article-date::attr(datetime)').get(),
        "writer": selector.css(".z--font-bold").css("*::text").get().strip()
        or "",
        "shares_count": share_total,
        "comments_count": comments_total,
        "summary": "".join(
            selector.css(
                ".tec--article__body > p:first-of-type *::text"
            ).getall()
        ),
        "sources": [
            i.strip()
            for i in selector.css("[class='tec--badge']::text").getall()
        ],
        "categories": [
            i.strip() for i in selector.css("#js-categories a::text").getall()
        ],
    }


# Requisito 5
def get_tech_news(amount):
    url = fetch("https://www.tecmundo.com.br/novidades")
    news_list = []

    while len(news_list) < amount:
        for link in scrape_novidades(url):
            if len(news_list) < amount:
                news = fetch(link)
                news_list.append(scrape_noticia(news))

        if len(news_list) < amount:
            next_link = scrape_next_page_link(url)
            url = fetch(next_link)
    create_news(news_list)
    return news_list
