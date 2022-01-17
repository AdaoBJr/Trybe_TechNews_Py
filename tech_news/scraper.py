import requests
import time
import parsel
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        resp = requests.get(url, timeout=3)
        if resp.status_code == 200:
            return resp.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(text=html_content)
    return selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    return selector.css(".z--container .tec--btn::attr(href)").get()


# Requisito 4
def get_url(selector):
    return selector.css("head > link[rel=canonical] ::attr(href)").get()


def get_title(selector):
    return selector.css("#js-article-title ::text").get()


def get_timestamp(selector):
    return selector.css("#js-article-date ::attr(datetime)").get()


def get_writer(selector):
    query = [
        ".tec--author__info__link::text",
        ".tec--timestamp a::text",
        "#js-author-bar > div p::text",
    ]
    for item in query:
        writer = selector.css(item).get()
        if writer is not None:
            return writer.strip()
    return None


def get_shares_count(selector):
    shares_count = selector.css(".tec--toolbar > div:nth-child(1)::text").get()
    if shares_count is not None:
        return shares_count.strip().split(" ")[0]

    return 0


def get_comments_count(selector):
    return selector.css("#js-comments-btn ::attr(data-count)").get()


def get_summary(selector):
    summary = "".join(
        selector.css(".tec--article__body > " "p:nth-child(1) ::text").getall()
    )
    if summary is not None:
        return summary

    return None


def get_sources(selector):
    sources = selector.css(".z--mb-16 > div > a::text").getall()
    if sources is not []:
        list_categories = list(map(lambda x: (x.strip()), sources))
        return list(filter(lambda x: x != "", list_categories))
    return None


def get_categories(selector):
    categories = selector.css("#js-categories ::text").getall()
    list_categories = list(map(lambda x: (x.strip()), categories))
    return list(filter(lambda x: x != "", list_categories))


def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    info = {}
    info["url"] = get_url(selector)
    info["title"] = get_title(selector)
    info["timestamp"] = get_timestamp(selector)
    info["writer"] = get_writer(selector)
    info["shares_count"] = int(get_shares_count(selector))
    info["comments_count"] = int(get_comments_count(selector))
    info["summary"] = get_summary(selector)
    info["sources"] = get_sources(selector)
    info["categories"] = get_categories(selector)
    return info


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(url)
    news_urls = scrape_novidades(html_content)
    tech_news = []

    while len(news_urls) < amount:
        next_page = scrape_next_page_link(html_content)
        html_content = fetch(next_page)
        news_urls.extend(scrape_novidades(html_content))

    for index in range(amount):
        news_url = news_urls[index]
        new_page = fetch(news_url)
        new_info = scrape_noticia(new_page)
        tech_news.append(new_info)

    create_news(tech_news)

    return tech_news
