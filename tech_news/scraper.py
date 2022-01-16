import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()
        return response.text
    except (requests.ReadTimeout, requests.exceptions.HTTPError):
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    list_links = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        + " div.tec--list.tec--list--lg article > div > h3 > a::attr(href)"
    ).getall()
    return list_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        + " div.tec--list.tec--list--lg > a::attr(href)"
    ).get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title ::text").get()
    timestamp = selector.css("#js-article-date ::attr(datetime)").get()
    writer = selector.css(".z--font-bold ::text").get()

    if writer:
        writer = writer.strip(" ")
    else:
        writer = None

    shares_count = selector.css(
        "#js-author-bar > nav > div:nth-child(1)" + " ::text"
    ).get()

    if shares_count:
        shares_count = int(shares_count.strip("Compartilharam"))
    else:
        shares_count = 0

    comments_count = selector.css(
        "#js-comments-btn" + " ::attr(data-count)"
    ).get()

    if comments_count:
        comments_count = int(comments_count.strip("Compartilharam"))
    else:
        comments_count = 0

    # https://pt.stackoverflow.com/questions/421678/juntar-elementos-de-uma-lista-com-o-%C3%BAltimo-separador-diferente
    summary = "".join(
        selector.css(
            "div.tec--article__body.p402_premium > p:nth-child(1) ::text"
        ).getall()
    )
    sources = with_out_space(
        selector.css(".z--mb-16 > div > a ::text").getall()
    )
    categories = with_out_space(
        selector.css("#js-categories > a::text").getall()
    )

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


def with_out_space(array):
    list = [item.strip(" ") for item in array]
    return list
