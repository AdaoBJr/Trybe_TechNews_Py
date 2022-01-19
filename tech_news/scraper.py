import requests
import time
import re
from parsel import Selector
from tech_news.database import create_news

COLLECTOR = {
    "news": "#js-main .tec--card__title__link::attr(href)",
    "next": "#js-main .tec--btn::attr(href)",
    "url": "link[rel=canonical]::attr(href)",
    "title": "#js-article-title::text",
    "writer": ".z--font-bold",
    "shares_number": "#js-author-bar div:nth-child(1)::text",
    "comments_number": "#js-comments-btn::attr(data-count)",
    "sumary": "div.tec--article__body > p:nth-child(1) *::text",
    "sources": ".z--mb-16 .tec--badge::text",
    "categories": ".tec--badge--primary::text",
    "timestamp": "#js-article-date::attr(datetime)",
}


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        request = requests.get(url, timeout=3)
        if request.status_code == 200:
            return request.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    if html_content == "":
        return list()
    else:
        selector = Selector(text=html_content)
        links = selector.css("h3 a::attr(href)").getall()
        return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    if html_content == "":
        return None
    else:
        selector = Selector(html_content)
        next_page_link = selector.css(".tec--list > a::attr(href)").get()
        return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    """Requesito 4 feito com base o projeto do Anderson Turkiewicz"""
    content = Selector(html_content)
    shares_number = content.css(COLLECTOR["shares_number"]).get() or "0"
    comments_number = content.css(COLLECTOR["comments_number"]).get() or "0"
    return {
        "title": content.css(COLLECTOR["title"]).get(),
        "url": content.css(COLLECTOR["url"]).get(),
        "writer": content.css(".z--font-bold").css("*::text").get().strip()
        or "",
        "shares_count": int(re.sub("[^0-9]", "", shares_number)),
        "comments_count": int(comments_number),
        "summary": "".join(content.css(COLLECTOR["sumary"]).getall()),
        "sources": [
            text.strip()
            for text in (content.css(COLLECTOR["sources"]).getall())
        ],
        "categories": [
            text.strip()
            for text in (content.css(COLLECTOR["categories"]).getall())
        ],
        "timestamp": content.css(COLLECTOR["timestamp"]).get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = fetch("https://www.tecmundo.com.br/novidades")
    news = scrape_novidades(url)
    next_page_url = scrape_next_page_link(url)

    while len(news) < amount:
        url = fetch(next_page_url)
        news += scrape_novidades(url)

    scraped_news = []
    for n in news[:amount]:
        html_news = fetch(n)
        scraped_news.append(scrape_noticia(html_news))

    create_news(scraped_news)

    return scraped_news
