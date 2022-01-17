import requests
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""


""" with open("url.txt", "r") as reader:
    link_noticia = reader.readline()
    html_page_content = fetch(link_noticia)
    scrape_noticia(html_page_content) """
