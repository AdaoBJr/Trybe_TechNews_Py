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


def getShareCount(share):
    if(share is None):
        return 0
    return int(share[1])


def getSources(sources):
    sourceArr = []
    for source in sources:
        sourceArr.append(source[1:-1])
    return sourceArr


def getCategorie(categories):
    catArr = []
    for categorie in categories:
        catArr.append(categorie[1:-1])
    return catArr


# Requisito 4
def scrape_noticia(html_content):
    selec = Selector(text=html_content)
    scrapedNews = {}

    scrapedNews['url'] = selec.css(
        'head > link[rel=canonical]::attr(href)'
    ).get().strip()

    scrapedNews['title'] = selec.css(
        'h1.tec--article__header__title::text'
    ).get()

    scrapedNews['timestamp'] = selec.css(
        'div.tec--timestamp__item > time::attr(datetime)'
    ).get()

    scrapedNews['writer'] = getWriter(
        selec.css('.tec--article__body-grid .z--font-bold a::text').get(),
        selec)

    scrapedNews['shares_count'] = getShareCount(
        selec.css('div.tec--toolbar__item::text').get())

    scrapedNews['comments_count'] = int(selec.css(
        '#js-comments-btn::attr(data-count)').get())

    scrapedNews['summary'] = "".join(selec.css(
        '.tec--article__body > p:nth-child(1) *::text').getall())

    scrapedNews['sources'] = getSources(
        selec.css('.z--mb-16 > div > a::text').getall())

    scrapedNews['categories'] = getCategorie(
        selec.css("#js-categories a::text").getall())

    return scrapedNews


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
