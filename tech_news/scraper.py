from parsel import Selector
from .database import create_news
import requests
import time


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    if html_content == "":
        return list()
    else:
        selector = Selector(text=html_content)
        links = selector.css(
            'h3 a::attr(href)').getall()
        return links


# Requisito 3
def scrape_next_page_link(html_content):
    if html_content == "":
        return None
    else:
        selector = Selector(html_content)
        next_page_link = selector.css('.tec--list > a::attr(href)').get()
        return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    links = selector.css('head link').xpath('@href').getall()

    matching = [s for s in links if "https://www.tecmundo.com.br" in s]
    url = matching[1]

    timestamp = selector.css(
        '.tec--timestamp__item > time::attr(datetime)').get()

    shares_count = selector.css(
        '.tec--toolbar > .tec--toolbar__item::text').get()
    if shares_count is None:
        shares_count = 0
    else:
        shares_count = int(shares_count[1])

    comments_count = int(selector.css(
        '#js-comments-btn::attr(data-count)').get())

    raw_categories = selector.css("#js-categories a::text").getall()
    categories = []
    for category in raw_categories:
        categories.append(category[1:-1])

    title = selector.css('#js-article-title::text').get()

    writer = selector.css(
        '.tec--article__body-grid .z--font-bold a::text').get()
    if writer is not None:
        writer = writer[1:-1]
    if writer is None:
        writer = selector.css('.tec--author__info > p::text').get()

    raw_sources = selector.css('.z--mb-16 > div > a::text').getall()
    sources = []
    for source in raw_sources:
        sources.append(source[1:-1])

    paragraph = selector.css(
        '.tec--article__body > p:first-child *::text').getall()
    summary = "".join(paragraph)

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
    BASE_URL = 'https://www.tecmundo.com.br/novidades'
    next_page = scrape_next_page_link(fetch(BASE_URL))
    response1 = fetch(BASE_URL)
    response2 = fetch(next_page)
    all_links = []
    links_page_1 = scrape_novidades(response1)
    links_page_2 = scrape_novidades(response2)
    for link in links_page_1:
        all_links.append(link)
    for link in links_page_2:
        all_links.append(link)
    selected_links = all_links[-abs(amount):-1]
    news = []
    for link in selected_links:
        response = scrape_noticia(fetch(link))
        news.append(response)
    create_news(news)
    return news
