# Requisito 1
import requests
import time
from parsel import Selector
from tech_news.database import create_news


def fetch(url):
    time.sleep(1)
    try:
        if requests.get(url, timeout=3).status_code == 200:
            get_url = requests.get(url, timeout=3)
            html_content = get_url.text
            return html_content
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links = selector.css(".tec--list--lg .tec--card__title > a ::attr(href)")
    link_notices = links.getall()
    return link_notices


# Requisito 3
def scrape_next_page_link(html_content):
    if html_content == "":
        return None
    else:
        sel = Selector(html_content)
        next_pg = sel.css(".tec--list--lg  .tec--btn--primary::attr(href)")
        return next_pg.get()


def no_spaces(list):
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

    # https://stackoverflow.com/questions/30083949/how-to-join-list-in-python-but-make-the-last-separator-different
    summary = "".join(
        selector.css(".tec--article__body > p:nth-child(1) *::text").getall()
    )

    sources = no_spaces(selector.css(".z--mb-16 > div > a ::text").getall())

    categories = no_spaces(selector.css("#js-categories > a::text").getall())

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
    fetch_tecmundo = fetch("https://www.tecmundo.com.br/novidades")
    news = scrape_novidades(fetch_tecmundo)
    new_news = []

    while len(new_news) < amount:
        for link in news:
            fetch_tecmundo = fetch(link)
            if fetch_tecmundo:
                new_news.append(scrape_noticia(fetch_tecmundo))
            else:
                continue
        if scrape_next_page_link(fetch_tecmundo):
            fetch_tecmundo = fetch(scrape_next_page_link(fetch_tecmundo))
            news = scrape_novidades(fetch_tecmundo)
        else:
            break

    create_news(new_news)
    return new_news
