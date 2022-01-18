import requests
import time
from parsel import Selector
from tech_news.database import create_news
# Requisito 1 - Iniciando o Projeto Tech News


def fetch(url):
    try:
        res = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.Timeout:
        return None
    if res.status_code == 200:
        return res.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    url_news = selector.css("div > h3 > a ::attr(href)").getall()
    return url_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    btn_next_page = selector.css("a.tec--btn--primary ::attr(href)").get()
    if btn_next_page:
        return btn_next_page
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer = selector.css(".z--font-bold ::text").get()
    if writer:
        writer = writer.strip()
    else:
        writer = None

    shares_count = selector.css(
        ".tec--toolbar > .tec--toolbar__item::text"
    ).get()
    if shares_count:
        shares_count = int(shares_count.strip("Compartilharam"))
    else:
        shares_count = 0

    comments_count = selector.css(
        ".tec--toolbar__item > button::attr(data-count)"
        ).get()

    if comments_count:
        comments_count = int(comments_count.strip("Comentários"))
    else:
        comments_count = 0

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
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 5
def get_tech_news(amount):
    news_page = fetch("https://www.tecmundo.com.br/novidades")
    new_url_list = scrape_novidades(news_page)
    result = []
    while len(result) < amount:
        for news in new_url_list:
            news_page = fetch(news)
            if news_page:
                result.append(scrape_noticia(news_page))
        if scrape_next_page_link(news_page):
            news_page = fetch(scrape_next_page_link(news_page))
            new_url_list = scrape_novidades(news_page)
        else:
            break

    create_news(result)
    return result
