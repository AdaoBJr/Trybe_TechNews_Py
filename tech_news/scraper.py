import requests
from parsel import Selector
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    if html_content == "" or html_content is None:
        return list()
    selector = Selector(text=html_content)
    novidades_urls_list = selector.css(
        ".tec--card__info h3 a::attr(href)").getall()
    return novidades_urls_list


# Requisito 3
def scrape_next_page_link(html_content):
    if html_content == "":
        return None
    selector = Selector(text=html_content)
    next_page_url = selector.css("div.tec--list > a::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(
        "h1.tec--article__header__title::text").get()
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)").get()
    writer = selector.css(".tec--author__info a::text").get() or None
    shares_count = selector.css(
        "div.tec--toolbar__item::text").get() or 0
    shares_count = shares_count.strip(" Compartilharam ")
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = selector.css(
        ".tec--article__body > p:nth-child(1) *::text").getall()
    summary_text = ""
    for sum in summary:
        summary_text = summary_text + sum
    sources = selector.css(".z--mb-16 a.tec--badge::text").getall()
    categories = selector.css("#js-categories a::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary_text,
        "sources": sources,
        "categories": categories
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
