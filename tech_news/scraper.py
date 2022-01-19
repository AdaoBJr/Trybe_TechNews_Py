import requests
import time
from parsel import Selector
from tech_news.database import create_news


def remove_spaces(array):
    new_array = []
    for item in array:
        new_array.append(item.strip())
    return new_array


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
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
    url_news = selector.css('article > div > h3 > a::attr(href)').getall()
    return url_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    btn_more_news = selector.css('a.tec--btn--primary::attr(href)').get()
    if btn_more_news:
        return btn_more_news
    else:
        return None


# Requisito 4
# agradecimento ao amigo Rafael Mathias e ao Will Marcondes pela ajuda
def scrape_noticia(html_content):
    selector = Selector(html_content)
    
    url = selector.css(
        "link[rel=canonical]::attr(href)"
        ).get()

    title = selector.css(
        "h1.tec--article__header__title::text"
        ).get()

    timestamp = selector.css(
        "#js-article-date::attr(datetime)"
        ).get()

    writer = selector.css(
        ".z--font-bold ::text"
    ).get()

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

    summary = "".join(selector.css(
        ".tec--article__body > p:nth-child(1) *::text"
        ).getall())

    sources = remove_spaces(selector.css(
        ".z--mb-16 div a::text"
        ).getall())

    categories = remove_spaces(selector.css(
        "#js-categories a::text"
        ).getall())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories
    }


# Requisito 5
def get_tech_news(amount):
    html_text = fetch('https://www.tecmundo.com.br/novidades')
    news = scrape_novidades(html_text)
    scraped_news = []

    while len(scraped_news) < amount:
        for link in news:
            html_text = fetch(link)
            if html_text:
                scraped_news.append(scrape_noticia(html_text))
            else:
                continue
        if scrape_next_page_link(html_text):
            html_text = fetch(scrape_next_page_link(html_text))
            news = scrape_novidades(html_text)
        else:
            break
    create_news(scraped_news)
    return scraped_news


def testar_manualmente(index):
    from tests.assets.test_assets import (
        all_news,
    )
    url = all_news[index]['url']
    html_content = fetch(url)
    print(scrape_noticia(html_content))