from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        resp = requests.get(url, timeout=3)
        resp.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    else:
        if (resp.status_code == 200):
            return resp.text


# Requisito 2
def scrape_novidades(html_content):
    selec = Selector(text=html_content)
    listLinks = selec.css(
        '.tec--card__info h3 .tec--card__title__link::attr(href)'
    ).getall()

    return listLinks


# Requisito 3
def scrape_next_page_link(html_content):
    selec = Selector(text=html_content)
    nextLink = selec.css('div.tec--list > a::attr(href)').get()
    return nextLink


def getWriter(writer, selec):
    if writer is not None:
        return writer[1:-1]
    if writer is None:
        return selec.css('.tec--author__info > p::text').get()


# Requisito 4
def scrape_noticia(html_content):
    selec = Selector(text=html_content)
    scrapedNews = {}

    scrapedNews['url'] = selec.css(
        'head > link[rel=canonical]::attr(href)'
    ).get().strip()

    scrapedNews['title'] = selec.css(
        'h1.tec--acticle__header__title::text'
    ).get()

    scrapedNews['timestamp'] = selec.css(
        'div.tec--timestamp__item > time::attr(datetime)'
    ).get()

    scrapedNews['writer'] = getWriter(
        selec.css('.tec--article__body-grid .z--font-bold a::text').get(),
        selec)

    scrapedNews['']

    return scrapedNews


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
