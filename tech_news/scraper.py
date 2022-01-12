import requests
import time
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_url_list = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        "div.tec--list.tec--list--lg div > h3 > a ::attr(href)"
    ).getall()
    return news_url_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 > "
        "div.tec--list.tec--list--lg > a ::attr(href)"
    ).get()
    if not next_page_url:
        return None
    return next_page_url


def format_list(original_list):
    new_list = []
    for word in original_list:
        if word != " ":
            word = word.strip()
            new_list.append(word)
    return new_list


def format_summary(original_summary):
    new_summary = ""
    for word in original_summary:
        new_summary += word

    return new_summary


def format_numbers(original_numbers):
    if not original_numbers:
        return 0
    else:
        return int(original_numbers)


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical] ::attr(href)").get()
    title = selector.css("#js-article-title ::text").get()

    timestamp = selector.css("#js-article-date ::attr(datetime)").get()

    writer = str(
        selector.css(
            "#js-author-bar > div >"
            "p.z--m-none.z--truncate.z--font-bold *::text"
        ).get()
    ).strip()

    if writer == "None":
        writer = str(
            selector.css(
                "#js-main > div > article > "
                "div.tec--article__body-grid > div.z--pt-40.z--pb-24 >"
                " div.z--flex.z--items-center > "
                "div.tec--timestamp.tec--timestamp--lg"
                " > div.tec--timestamp__item.z--font-bold > a ::text"
            ).get()
        ).strip()

    try:
        shares_count = (
            selector.css("#js-author-bar > nav > div:nth-child(1) ::text")
            .get()
            .strip()
            .split(" ")[0]
        )
    except AttributeError:
        shares_count = 0

    shares_count = format_numbers(shares_count)

    comments_count = selector.css("#js-comments-btn ::attr(data-count)").get()
    comments_count = format_numbers(comments_count)

    summary = selector.css(
        "#js-main > div > article > div.tec--article__body-grid >"
        "div.tec--article__body > p:nth-child(1) *::text"
    ).getall()
    summary = format_summary(summary)

    sources = selector.css(
        "#js-main > div > article >"
        "div.tec--article__body-grid > div.z--mb-16 > div ::text"
    ).getall()
    sources = format_list(sources)

    categories = selector.css("#js-categories ::text").getall()
    categories = format_list(categories)

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
    URL_BASE = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(URL_BASE)
    news_url_list = scrape_novidades(html_content)
    data = []

    while len(news_url_list) < amount:
        URL_BASE = scrape_next_page_link(html_content)
        html_content = fetch(URL_BASE)
        news_url_list.extend(scrape_novidades(html_content))

    for i in range(amount):
        news_url = news_url_list[i]
        news_html_content = fetch(news_url)
        data.append(scrape_noticia(news_html_content))

    create_news(data)
    return data
