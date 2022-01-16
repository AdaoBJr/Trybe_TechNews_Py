import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    css_selector = "article > div > h3 > a ::attr(href)"
    return selector.css(css_selector).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    css_selector = "div.tec--list.tec--list--lg > a ::attr(href)"
    return selector.css(css_selector).get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("head > link[rel=canonical] ::attr(href)").get()
    title = selector.css("#js-article-title ::text").get()
    timestamp = selector.css("#js-article-date ::attr(datetime)").get()
    try:
        writer = selector.css(".z--font-bold ::text").get().strip()
        try:
            selector_share = "#js-author-bar > nav > div:nth-child(1) ::text"
            shares_count = int(
                selector.css(selector_share)
                .get()
                .strip()
                .split(" ")[0]
            )
        except (AttributeError, ValueError):
            shares_count = 0
    except AttributeError:
        writer = ""

    css_selector_comments = "#js-comments-btn ::attr(data-count)"
    css_selector_summary = (
            "div.tec--article__body-grid"
            " > div.tec--article__body > p:nth-child(1) ::text"
        )
    comments_count = int(selector.css(css_selector_comments).get())
    summary = selector.css(css_selector_summary).getall()

    sources = selector.css(".z--mb-16 .tec--badge ::text").getall()
    categories = selector.css("#js-categories > a ::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": "".join(summary),
        "sources": [i.strip() for i in sources],
        "categories": [i.strip() for i in categories],
    }


# Requisito 5
def get_tech_news(amount):
    url = 'https://www.tecmundo.com.br/novidades'
    html_content = fetch(url)
    news_urls = scrape_novidades(html_content)
    news_list = []

    while len(news_urls) < amount:
        url = scrape_next_page_link(html_content)
        html_content = fetch(url)
        news_urls.extend(scrape_novidades(html_content))

    for index in range(amount):
        notice_url = news_urls[index]
        notice_page = fetch(notice_url)
        notice_info = scrape_noticia(notice_page)
        news_list.append(notice_info)

    create_news(news_list)
    return news_list
