import requests
import time
from parsel import Selector
import re


# Requisito 1
def fetch(url):
    try:
        res = requests.get(url, timeout=3)
        if res.status_code != 200:
            return None
        return res.text
    except requests.Timeout:
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_novidades(html_content):
    sel = Selector(text=html_content)
    link = ".tec--list h3 a::attr(href)"
    return sel.css(link).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    sel = Selector(text=html_content)
    return sel.css(".tec--list--lg .tec--btn::attr(href)").get()


# Requisito 4
def url(url):
    return url.css("head link[rel=canonical]::attr(href)").get()


def title(title):
    return title.css("h1::text").get()


def timestamp(timestamp):
    return timestamp.css("div time::attr(datetime)").get()


def writer(writer):
    sel = [
        ".tec--timestamp a::text",
        ".tec--author p:first-child::text",
        ".tec--author p a::text",
    ]
    result = []
    for selector in sel:
        select_writer = writer.css(selector).get()
        if select_writer is not None:
            result.append(select_writer.strip(' '))
        if select_writer is None:
            result.append(None)
    writer = [author for author in result if author]
    if len(writer) == 0:
        return None
    return writer[0]


def shares_count(count):
    shares = count.css("nav tec--toolbar div:first-child::text").get()
    if shares is None or not ("Compartilharam") in shares:
        return 0
    return int(count[re.findall(shares)])  # r'^# numbers:\s+(.*)$'


def comments_count(count):
    coment = count.css("button js-comments-btn::attr(data-count)").get()
    if coment is None:
        return 0
    return int(coment)


def summary(sumary):
    return ''.join(
        sumary.css(".tec--article__body p:nth-child(1) *::text").getall()
    )


def sources(sel):
    sources = sel.css(".z--mb-16 a::text").getall()
    return [source.strip() for source in sources]


def categories(category):
    categories = category.css("div #js-categories a::text").getall()
    return [category.strip() for category in categories]


def scrape_noticia(html_content):
    sel = Selector(text=html_content)
    info = {
        "url": url(sel),
        "title": title(sel),
        "timestamp": timestamp(sel),
        "writer": writer(sel),
        "shares_count": shares_count(sel),
        "comments_count": comments_count(sel),
        "summary": summary(sel),
        "sources": sources(sel),
        "categories": categories(sel),
    }

    return info


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# print(fetch("https://www.tecmundo.com.br/novidades/"))
# print(scrape_novidades("https://www.tecmundo.com.br/novidades/"))
# print(scrape_next_page_link("https://www.tecmundo.com.br/novidades/"))
# print(scrape_noticia(
#     "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
# ))
