# Requisito 1
import requests
import time
from parsel import Selector
import re


def fetch(url):
    """Seu código deve vir aqui"""
    try:

        response = requests.get(
            url, timeout=1
        )
        response.raise_for_status()
        return response.text
    except (requests.ReadTimeout, requests.exceptions.HTTPError):
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    links = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        + "div.tec--list.tec--list--lg article > div > h3 > a::attr(href)"
        ).getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page_link = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        + " div.tec--list.tec--list--lg > a::attr(href)"
    ).get()
    return next_page_link


# Requisito 4

def shares_count_func(selector): # pega o primeiro valor da string e converte para int
    answer = selector.css("div.tec--toolbar__item::text").get()
    if answer:
        answer = int(re.findall(r'\d+', answer)[0])
    else:
        answer = 0
    return answer


def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css(
        "div.tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = (
        selector.css(".z--font-bold").css("*::text").get().strip() or ""
    )
    shares_count = shares_count_func(selector)
    comments_count = selector.css(
        "button#js-comments-btn::attr(data-count)"
    ).get()
    get_summary = selector.css(
        "div.tec--article__body > p:nth-child(1) *::text"
    ).getall()
    summary = ''.join(get_summary)
    get_sources = selector.css("div.z--mb-16 div a::text").getall()
    sources = [item.strip() for item in get_sources]
    get_categories = selector.css("div#js-categories a::text").getall()
    categories = [item.strip() for item in get_categories]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
