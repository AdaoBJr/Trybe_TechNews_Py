import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        request = requests.get(url, timeout=1)
        if request.status_code != 200:
            return None
        return request.text
    except requests.Timeout:
        return None
    """Seu código deve vir aqui"""


# Requisito 2
# https://app.betrybe.com/course/computer-science/redes-e-raspagem-de-dados/raspagem-de-dados
# /ab38ab4e-bdbd-4984-8987-1abf32d85f26/conteudos/b63ffce8-be02-4be1-9b88-bda695400647/recursos-obtidos-a-partir-de-outro-recurso/45e6934f-7f20-41e4-bd56-e66f348c4685?use_case=side_bar
def scrape_novidades(html_content):
    selector = Selector(html_content)
    print(selector)
    return selector.css(".tec--list--lg h3 a::attr(href)").getall()
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    print(selector)
    return selector.css(".tec--list--lg > a::attr(href)").get()
    """Seu código deve vir aqui"""


def get_writers(writer1, writer2, writer3):
    if writer1 is not None:
        return writer1.strip()
    elif writer2 is not None:
        return writer2.strip()
    else:
        return writer3


def get_share_counters(counters):
    if counters is not None:
        for str in counters.split():
            if str.isdigit():
                return int(str)
    else:
        return 0


def get_sources(source1, source2):
    if len(source1):
        return [elem.strip() for elem in source1]
    else:
        return [x.strip(" ") for x in source2]


# https://stackoverflow.com/questions/3232953/python-removing-spaces-from-list-objects
# https://www.geeksforgeeks.org/python-extract-numbers-from-string/
# https://flexiple.com/check-if-list-is-empty-python/
# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news = selector

    source1 = news.css(".z--mb-16.z--px-16 .tec--badge::text").getall()
    source2 = news.css("div.tec--article__body-grid > \
                        div.z--mb-16 > div > a::text").getall()

    writer1 = news.css(".tec--author__info__link::text").get()
    writer2 = news.css(".tec--timestamp__item.z--font-bold a::text").get()
    writer3 = news.css("p.z--m-none.z--truncate.z--font-bold::text").get()
    shares_count = news.css(".tec--toolbar > div:nth-child(1)::text").get()

    news_cicle = {
        "url": news.css("link[rel=canonical]::attr(href)").get(),
        "title": news.css("#js-article-title::text").get(),
        "timestamp": news.css
                         (".tec--timestamp__item > time ::attr(datetime)").get
                         (),
        "writer": get_writers(writer1, writer2, writer3),
        "shares_count": get_share_counters(shares_count),
        "comments_count": int(news.css("#js-comments-btn::attr(data-count)").
                              get()),
        "summary": "".join(news.css
                           (".tec--article__body > p:nth-child(1) ::text").
                           getall()),
        "sources": get_sources(source1, source2),
        "categories": [x.strip(" ") for x
                       in news.css("#js-categories > a::text").getall()],
    }

    return news_cicle
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
