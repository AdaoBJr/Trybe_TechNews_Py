import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1


def fetch(url):

    try:
        time.sleep(1)
        page = requests.get(url, timeout=3)

        if page.status_code == 200:
            return page.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links = selector.css(
        "div.tec--card__info h3 a::attr(href)"
    ).getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    page = Selector(text=html_content).css(".tec--list > a::attr(href)").get()
    if page:
        return page
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    url = (
        Selector(text=html_content)
        .css("link[rel=canonical]::attr(href)")
        .get()
    )

    title = Selector(text=html_content).css("#js-article-title ::text").get()

    timestamp = (
        Selector(text=html_content)
        .css("#js-article-date ::attr(datetime)")
        .get()
    )

    try:
        writer = (
            Selector(text=html_content)
            .css(".z--font-bold")
            .css("*::text")
            .get()
            .strip()
            or ""
        )
    except AttributeError:
        writer = None

    try:
        shares_count = (
            Selector(text=html_content)
            .css(".tec--toolbar__item::text")
            .get()
            .strip()
            .split(" ")[0]
        )
    except AttributeError:
        shares_count = 0

    comments_count = (
        Selector(text=html_content).css(".tec--btn::attr(data-count)").get()
    )

    summary = "".join(
        Selector(text=html_content)
        .css(".tec--article__body > p:first-child *::text")
        .getall()
    )

    sources = (
        Selector(text=html_content).css(".z--mb-16 .tec--badge::text").getall()
    )

    categories = (
        Selector(text=html_content).css(".tec--badge--primary::text").getall()
    )

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(url)
    news = scrape_novidades(html_content)
    news_list = []

    while len(news) < amount:
        url = scrape_next_page_link(html_content)
        html_content = fetch(url)
        news.extend(scrape_novidades(html_content))

    for new_url in news[0:amount]:
        response = fetch(new_url)
        new = scrape_noticia(response)
        news_list.append(new)

    create_news(news_list)
    return news_list
