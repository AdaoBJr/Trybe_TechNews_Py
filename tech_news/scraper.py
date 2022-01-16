import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    sele = Selector(text=html_content)
    return sele.css(".tec--list .tec--card__title__link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get().strip()
    shares = selector.css(".tec--toolbar__item::text").get()
    if shares:
        shares_count = shares.split()[0]
    else:
        shares_count = 0

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    su = selector.css(".tec--article__body > p:first-of-type *::text").getall()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    source = [i.strip() for i in sources]
    categories = selector.css("#js-categories a::text").getall()
    category = [i.strip() for i in categories]

    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'shares_count': int(shares_count),
        'comments_count': int(comments_count),
        'summary': "".join(su),
        "sources": source,
        "categories": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
