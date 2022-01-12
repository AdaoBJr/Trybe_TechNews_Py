import requests
import time
from parsel import Selector
from .database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, timeout=3)
        if not res.status_code == 200:
            return None
        return res.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    result = selector.css(
        ".tec--list--lg .tec--card__title > a ::attr(href)"
    ).getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    result = selector.css(".tec--list.tec--list--lg > a ::attr(href)").get()
    return result


def get_url(html_content):
    selector = Selector(html_content)
    result = selector.css("head > link[rel=canonical] ::attr(href)").get()
    return result


def get_title(html_content):
    selector = Selector(html_content)
    result = selector.css("#js-article-title ::text").get()
    return result


def get_timestamp(html_content):
    selector = Selector(html_content)
    result = selector.css("#js-article-date ::attr(datetime)").get()
    return result


def get_writer(html_content):
    selector = Selector(text=html_content)
    query = [
        ".tec--timestamp__item.z--font-bold ::text",
        ".tec--author__info__link ::text",
        "div > p.z--m-none.z--truncate.z--font-bold::text",
    ]

    for i in query:
        item = selector.css(i).get()
        if item is not None:
            return item.strip()
    return None


def get_shares_count(html_content):
    selector = Selector(html_content)
    shares_text = selector.css(".tec--toolbar > div:nth-child(1)::text").get()
    if shares_text is not None:
        shares_value = shares_text.strip().split(" ")[0]
        return int(shares_value)
    return 0


def get_comments_count(html_content):
    selector = Selector(html_content)
    result = int(selector.css("#js-comments-btn ::attr(data-count)").get())
    return result


def get_summary(html_content):
    selector = Selector(html_content)
    summary = "".join(
        selector.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )
    if summary is not None:
        return summary
    return None


def get_sources(html_content):
    selector = Selector(html_content)
    query = [
        ".z--mb-16 > div > a ::text",
        ".z--mb-16.z--px-16 > div ::text",
    ]

    for i in query:
        item_list = selector.css(i).getall()
        if item_list is not []:
            item_list_wo_space = list(map(lambda x: x.strip(), item_list))
            return list(filter(lambda x: x != "", item_list_wo_space))
    return None


def get_categories(html_content):
    selector = Selector(html_content)
    categories = selector.css("#js-categories ::text").getall()
    categories_wo_space = list(map(lambda x: x.strip(), categories))
    return list(filter(lambda x: x != "", categories_wo_space))


# ajuda de Pedro Henrique Pires
# PR: https://github.com/tryber/sd-010-b-tech-news/pull/5
# Requisito 4
def scrape_noticia(html_content):
    scrape_dict = {}
    scrape_dict["url"] = get_url(html_content)
    scrape_dict["title"] = get_title(html_content)
    scrape_dict["timestamp"] = get_timestamp(html_content)
    scrape_dict["writer"] = get_writer(html_content)
    scrape_dict["shares_count"] = get_shares_count(html_content)
    scrape_dict["comments_count"] = get_comments_count(html_content)
    scrape_dict["summary"] = get_summary(html_content)
    scrape_dict["sources"] = get_sources(html_content)
    scrape_dict["categories"] = get_categories(html_content)
    return scrape_dict


# Requisito 5
def get_tech_news(amount):
    html_content = fetch("https://www.tecmundo.com.br/novidades")
    url_list = scrape_novidades(html_content)
    noticias_list = []

    while len(url_list) < amount:
        new_url = scrape_next_page_link(html_content)
        new_html_content = fetch(new_url)
        url_list += scrape_novidades(new_html_content)

    for value in range(amount):
        url_noticia = fetch(url_list[value])
        noticia_dados = scrape_noticia(url_noticia)
        noticias_list += [noticia_dados]

    create_news(noticias_list)
    return noticias_list
