# Requisito 1
import time
import requests
from parsel import Selector
from tech_news.database import create_news


def fetch(url):
    time.sleep(1)

    try:
        res = requests.get(url, timeout=3)
        res.raise_for_status()

    except requests.Timeout:
        return None
    except requests.HTTPError:
        return None

    return res.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    res = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        "div.tec--list.tec--list--lg  article > div > h3 > a::attr(href)"
    )
    return res.getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    res = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        " div.tec--list.tec--list--lg > a::attr(href)"
    )
    return res.get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer = selector.css(".z--font-bold").css("*::text").get().strip() or ""

    try:
        shares_count = (
            selector.css(".tec--toolbar__item::text")
            .get()
            .strip()
            .split(" ")[0]
        )
    except AttributeError:
        shares_count = 0

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()

    summary = "".join(
        selector.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )

    sources = selector.css(".z--mb-16 .tec--badge::text").getall()

    categories = selector.css("#js-categories > a::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 5
def get_tech_news(amount):
    content = fetch("https://www.tecmundo.com.br/novidades")
    news_list = scrape_novidades(content)

    while len(news_list) < amount:
        new_url = scrape_next_page_link(content)
        new_content = fetch(new_url)
        news_list.extend(scrape_novidades(new_content))

    result = []

    for report in news_list[0:amount]:
        data = fetch(report)
        report = scrape_noticia(data)
        result.append(report)

    create_news(result)

    return result
