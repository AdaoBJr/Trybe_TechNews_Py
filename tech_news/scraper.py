import requests
import time
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        r = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    else:
        if r.status_code != 200:
            return None
        return r.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    # agradecimentos ao Gabriel Essênio pela ajuda
    # na compreensão dos seletores na função css
    return selector.css(
        ".tec--list--lg .tec--card__title > a ::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    if html_content == "":
        return None

    selector = Selector(html_content)
    return selector.css(".tec--list--lg .tec--btn--primary::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = {"url": selector.css("link[rel=canonical]").xpath("@href").get()}
    title = {"title": selector.css("h1::text").get()}
    timestamp = {"timestamp": selector.css("time::attr(datetime)").get()}
    writer = {"writer": selector.css(".z--font-bold *::text").get().strip()}
    shares_count_res = (
        selector.css("#js-author-bar > nav > div:first-child::text").re_first(
            r"\d+"
        )
        or 0
    )
    shares_count = {"shares_count": int(shares_count_res)}
    comments_count = {
        "comments_count": int(
            selector.css("#js-comments-btn::text").re_first(r"\d+")
        )
    }
    summary_str_list = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    summary = {"summary": "".join(summary_str_list)}
    sources = {
        "sources": [
            source.strip()
            for source in selector.css(".z--mb-16 > div > a::text").getall()
        ]
    }
    categories = {
        "categories": [
            category.strip()
            for category in selector.css("#js-categories a::text").getall()
        ]
    }
    scrape_res_list = [
        url,
        title,
        timestamp,
        writer,
        shares_count,
        comments_count,
        summary,
        sources,
        categories,
    ]

    scraped_news_dict = {}

    for d in scrape_res_list:
        scraped_news_dict.update(d)

    return scraped_news_dict


# Requisito 5
def get_tech_news(amount):
    news_urls_list = []
    url = "https://www.tecmundo.com.br/novidades"
    while len(news_urls_list) < amount:
        html_content = fetch(url)
        urls_list = scrape_novidades(html_content)
        max_news_per_page = len(urls_list)
        calc = amount - len(news_urls_list) - max_news_per_page
        if calc < 0:
            end_index = max_news_per_page + calc
            news_urls_list.extend(urls_list[:end_index])
        else:
            news_urls_list.extend(urls_list)

        if len(news_urls_list) < amount:
            url = scrape_next_page_link(html_content)

    news_to_insert = []

    for news_url in news_urls_list:
        html_content = fetch(news_url)
        scraped_news = scrape_noticia(html_content)
        news_to_insert.append(scraped_news)

    create_news(news_to_insert)
    return news_to_insert
