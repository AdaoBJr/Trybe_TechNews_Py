import requests
import time
from parsel import Selector


# função para remover espaços de cada string do array utilizada no requisito 4
def remove_spaces(array):
    new_array = []
    for item in array:
        new_array.append(item.strip())
    return new_array


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news = selector.css("div.tec--list")
    get_links_of_news = news.css(
        "figure a.tec--card__thumb__link::attr(href)"
    ).getall()
    return get_links_of_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(
        "div.tec--list > a.tec--btn::attr(href)"
        ).get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    # URL
    url = selector.css(
        "link[rel=canonical]::attr(href)"
        ).get()

    # TITLE
    title = selector.css(
        "h1.tec--article__header__title::text"
        ).get()

    # TIMESTAMP
    timestamp = selector.css(
        "#js-article-date::attr(datetime)"
        ).get()

    # WRITER
    writer = selector.css(
        ".z--font-bold ::text"
    ).get()

    if writer:
        writer = writer.strip()
    else:
        writer = None

    # SHARES COUNT
    shares_count = selector.css(
        ".tec--toolbar > .tec--toolbar__item::text"
        ).get()

    if shares_count:
        shares_count = int(shares_count.strip("Compartilharam"))
    else:
        shares_count = 0

    # COMMENTS COUNT
    comments_count = selector.css(
        ".tec--toolbar__item > button::attr(data-count)"
        ).get()

    if comments_count:
        comments_count = int(comments_count.strip("Comentários"))
    else:
        comments_count = 0

    # SUMMARY
    # https://stackoverflow.com/questions/30083949/how-to-join-list-in-python-but-make-the-last-separator-different
    summary = "".join(selector.css(
        ".tec--article__body > p:nth-child(1) *::text"
        ).getall())

    # SOURCES
    sources = remove_spaces(selector.css(
        ".z--mb-16 div a::text"
        ).getall())

    # CATEGORIES
    # remover espacos em branco
    categories = remove_spaces(selector.css(
        "#js-categories a::text"
        ).getall())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
