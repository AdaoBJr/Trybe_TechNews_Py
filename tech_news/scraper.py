import requests
import time
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        data = requests.get(url)
        data.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    else:
        return data.text


# Requisito 2
def scrape_novidades(html_content):
    element = Selector(html_content)

    return element.css("div.tec--card__info > h3 > a ::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    element = Selector(html_content).css(".tec--btn--lg::attr(href)").get()
    return element


# Requisito feito com a ajuda do João

# Requisito 4
def scrape_noticia(html_content):
    try:
        element = Selector(html_content)
        url = element.css("link[rel='canonical']::attr(href)").get()
        title = element.css(".tec--article__header__title::text").get()
        date = element.css("#js-article-date::attr(datetime)").get()
        write = element.css(".z--font-bold *::text").get().strip()
        counter_comments = element.css(".tec--btn::attr(data-count)").get()
        counter_share = (
            element.css(".tec--toolbar__item::text")
            .get()
            .lstrip()
            .split()[:2][0]
        )

    except AttributeError:
        counter_share = 0

    summary = "".join(
        element.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )

    sources = element.css(".z--mb-16 .tec--badge::text").getall()
    categories = element.css("#js-categories > a::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": date,
        "writer": write,
        "shares_count": int(counter_share),
        "comments_count": int(counter_comments),
        "summary": summary,
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
