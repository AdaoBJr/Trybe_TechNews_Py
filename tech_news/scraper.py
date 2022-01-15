import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.exceptions.RequestException:
        return None
    else:
        if response.status_code == 200:
            return response.text
    return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    news = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    moreNews = selector.css(".tec--btn::attr(href)").get()
    return moreNews


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    url_selected = selector.css("link[rel=canonical]::attr(href)").get()

    title_selected = selector.css(".tec--article__header__title::text").get()

    timestamp_selected = selector.css("time::attr(datetime)").get()

    writer_selected = (
        selector.css(".z--font-bold").css("*::text").get().strip() or ""
    )

    try:
        shares_count = (
            selector.css(".tec--toolbar__item::text")
            .get()
            .strip()
            .split(" ")[0]
        )
    except AttributeError:
        shares_count = 0

    comments_count = selector.css(".tec--btn::attr(data-count)").get()

    summary_selected = "".join(
        selector.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )

    sources_selected = selector.css(".z--mb-16 .tec--badge::text").getall()

    categories_selected = selector.css(".tec--badge--primary::text").getall()

    return {
        "url": url_selected,
        "title": title_selected,
        "timestamp": timestamp_selected,
        "writer": writer_selected,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary_selected,
        "sources": [source.strip() for source in sources_selected],
        "categories": [category.strip() for category in categories_selected],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
