import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    list_news = selector.css("div.tec--list")
    elements = list_news.css(
        "figure a.tec--card__thumb__link::attr(href)"
    ).getall()
    return elements


# Requisito 3
def scrape_next_page_link(html_content):
    if html_content == "":
        return None
    else:
        selector = Selector(text=html_content)
        return selector.css(
            ".tec--list--lg  .tec--btn--primary::attr(href)"
        ).get()


def no_empty_spaces(list):
    list_no_spaces = [space.strip(" ") for space in list]
    return list_no_spaces


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title ::text").get()

    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".z--font-bold ::text").get()

    shares_count = selector.css(
        ".tec--toolbar > .tec--toolbar__item::text"
    ).get()
    comments_count = selector.css(
        ".tec--toolbar__item > button::attr(data-count)"
    ).get()

    if writer:
        writer = writer.strip(" ")
    else:
        writer = None

    if shares_count:
        shares_count = int(shares_count.strip("Compartilharam"))
    else:
        shares_count = 0

    if comments_count:
        comments_count = int(comments_count.strip("Comentários"))
    else:
        comments_count = 0

    # consultado para usar o join
    # https://stackoverflow.com/questions/30083949/how-to-join-list-in-python-but-make-the-last-separator-different
    summary = "".join(
        selector.css(".tec--article__body > p:nth-child(1) *::text").getall()
    )

    sources = no_empty_spaces(
        selector.css(".z--mb-16 > div > a ::text").getall()
    )

    categories = no_empty_spaces(
        selector.css("#js-categories > a::text").getall()
    )

    result = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

    return result


# Requisito 5
def get_tech_news(amount):
    content_fetch = fetch("https://www.tecmundo.com.br/novidades")

    news_list = scrape_novidades(content_fetch)

    list_result = []

    while len(list_result) < amount:
        for element in news_list:
            content_fetch = fetch(element)

            if content_fetch:
                list_result.append(scrape_noticia(content_fetch))

        if scrape_next_page_link(content_fetch):

            content_fetch = fetch(content_fetch)

            news_list = scrape_novidades(content_fetch)
        else:
            break

    create_news(list_result)
    return list_result
