import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.Timeout:
        return None
    return response.text if response.status_code == 200 else None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_url = selector.css("h3 > a::attr(href)").getall()
    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_btn = selector.css(".tec--btn--primary::attr(href)").get()
    return next_page_btn


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = (
        selector.css(".z--font-bold").css("*::text").get().strip() or " ".get()
    )
    try:
        shares_count = selector.css(".tec--toolbar__item::text").get()\
            .strip().split(" ")[0]
    except AttributeError:
        shares_count = 0
    comments_count = int(
        selector.css(".tec--toolbar__item > button ::attr(data-count)").get()
    )
    summary = "".join(
        selector.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories a ::text").getall()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 5
def get_tech_news(amount):
    page = fetch("https://www.tecmundo.com.br/novidades")
    url_list = scrape_novidades(page)

    while len(url_list) < amount:
        next_page = scrape_next_page_link(page)
        new_url = fetch(next_page)
        more_url = scrape_novidades(new_url)
        url_list.extend(more_url)

    result = []

    for url in url_list[0:amount]:
        page_news = fetch(url)
        news_content = scrape_noticia(page_news)
        result.append(news_content)

    create_news(result)
    return result
