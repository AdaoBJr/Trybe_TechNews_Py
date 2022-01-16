import requests
from parsel import Selector
import time
from requests.exceptions import ReadTimeout


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
    seletor = Selector(html_content).css(
        'h3 .tec--card__title__link::attr(href)').getall()
    return seletor


# Requisito 3
def scrape_next_page_link(html_content):
    seletor = Selector(html_content).css(
        "div.tec--list--lg a.tec--btn--lg::attr(href)").get()
    return seletor


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
    return ''.join(new_item)


# Requisito 4
def scrape_noticia(html_content):
    if html_content == "":
        return []
    noticia = Selector(html_content)
    title = noticia.css('.tec--article__header__title::text').get()
    timestamp = noticia.css('.tec--timestamp__item time::attr(datetime)').get()
    writer = noticia.css('.tec--author__info__link::text').get() or None
    shares_count = noticia.css('.tec--toolbar__item::text').get() or 0
    comments_count = noticia.css(
        '.tec--toolbar__item #js-comments-btn::attr(data-count)').get()
    summary = noticia.css('.tec--article__body p').get()
    sources = noticia.css('.z--mb-16 div a.tec--badge::text').getall()
    categories = noticia.css(
        '#js-categories .tec--badge--primary::text').getall()
    fullinfo = {
        # "url": url,
        "categories": rm_space(categories),
        "comments_count": int(comments_count),
        "shares_count": int(shares_count.replace('Compartilharam', '')),
        "sources": rm_space(sources),
        "summary": rm_tags(summary),
        "timestamp": timestamp,
        "title": title,
        "writer": writer.strip()
    }
    return fullinfo


# Requisito 5
def get_tech_news(amount):
    # Seu código aqui
    return None
