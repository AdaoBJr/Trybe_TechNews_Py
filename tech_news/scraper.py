import requests
from parsel import Selector
import time
from requests.exceptions import ReadTimeout
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        request = requests.get(url, timeout=3)
        if request.status_code != 200:
            return None
        return request.text
    except ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    if html_content == "":
        return []
    noticias = Selector(html_content).css(
        'h3 .tec--card__title__link::attr(href)').getall()
    return noticias


# Requisito 3
def scrape_next_page_link(html_content):
    link_proxima_pagina = Selector(html_content).css(
        "div.tec--list--lg a.tec--btn--lg::attr(href)").get()
    return link_proxima_pagina


def rm_space(array):
    result = []
    for item in array:
        new_item = item.strip()
        result.append(new_item)
    return result


def rm_tags(item):
    is_remove = False
    new_item = []
    for carac in item:
        if carac == '<':
            is_remove = True
        if is_remove is False:
            new_item.append(carac)
        if carac == '>':
            is_remove = False
    return ''.join(item)


def search_autor(writer1, writer2, writer3):
    if writer1 is not None:
        return writer1.strip()
    elif writer2 is not None:
        return writer2.strip()
    elif writer3 is not None:
        return writer3.strip()


def object_noticia(html_content):
    noticia = Selector(html_content)
    url = noticia.css("head [rel='canonical']").css("link::attr(href)").get()
    title = noticia.css('.tec--article__header__title::text').get()
    timestamp = noticia.css('.tec--timestamp__item time::attr(datetime)').get()
    writer1 = noticia.css('.tec--author__info__link::text').get() or None
    writer2 = noticia.css(
        '.tec--timestamp .tec--timestamp__item a::text').get() or None
    writer3 = noticia.css(
        '.tec--author__info .z--font-bold::text').get() or None
    shares_count = noticia.css('.tec--toolbar__item::text').get() or 0
    comments_count = noticia.css(
        '.tec--toolbar__item #js-comments-btn::attr(data-count)').get()
    summary = noticia.css(
        '.tec--article__body p:nth-child(1) *::text').getall()
    sources = noticia.css('.z--mb-16 div a.tec--badge::text').getall()
    categories = noticia.css(
        '#js-categories .tec--badge--primary::text').getall()
    return {
        "url": url,
        "categories": rm_space(categories),
        "comments_count": comments_count,
        "shares_count": shares_count,
        "sources": rm_space(sources),
        "summary": rm_tags(summary),
        "timestamp": timestamp,
        "title": title,
        "writer": search_autor(writer1, writer2, writer3)
    }


# Requisito 4
def scrape_noticia(html_content):
    noticias = object_noticia(html_content)
    if noticias["shares_count"]:
        shares_count_replaced = noticias["shares_count"].replace(
            'Compartilharam', '')
        shares_count_int = int(shares_count_replaced)
        noticias["shares_count"] = shares_count_int
    if type(noticias["comments_count"]) is str:
        print('AMIGO ESTOU AQUI')
        noticias["comments_count"] = int(noticias["comments_count"])
    return noticias


# Requisito 5
def get_tech_news(amount):
    url_base = "https://www.tecmundo.com.br/novidades"
    noticias_link = []
    search_noticias = []
    noticias = []
    while len(noticias_link) < amount:
        html_content = fetch(url_base)
        noticias_link.extend(scrape_novidades(html_content))
        url_base = scrape_next_page_link(html_content)
    for index, noticia in enumerate(noticias_link):
        print(index, noticia)
        search_noticias.append(noticia)
        if (index + 1) == amount:
            break
    for noticia in search_noticias:
        html_content = fetch(noticia)
        result_noticia = scrape_noticia(html_content)
        noticias.append(result_noticia)
    create_news(noticias)
    return noticias
