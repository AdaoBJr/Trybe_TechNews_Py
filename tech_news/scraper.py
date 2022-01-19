from parsel import Selector
import requests
import time
from tech_news.database import create_news


def extractNumbers(string):
    return int(''.join(filter(str.isdigit, string)))


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (requests.exceptions.HTTPError, requests.Timeout):
        return None

    time.sleep(1)
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    try:
        return selector.css("div.tec--card__info h3 a::attr(href)").getall()
    except AttributeError:
        return None


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    try:
        return selector.css(".tec--btn--primary::attr(href)").get()
    except AttributeError:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news = {}

    url = selector.css("link[rel='canonical']::attr(href)").get()

    title = selector.css("h1.tec--article__header__title::text").get()

    timestamp = selector.css(
        "div.tec--timestamp__item time::attr(datetime)").get()

    try:
        writer = selector.css(
            ".z--font-bold").css("*::text").get().strip() or ""
    except AttributeError:
        writer = None

    try:
        shares_count = selector.css(
            ".tec--toolbar__item::text").get().strip().split(" ")[0]
    except AttributeError:
        shares_count = 0

    comments_count = selector.css(
        ".tec--btn::attr(data-count)").get()

    summary = selector.css(
        ".tec--article__body > p:first-child *::text").getall()

    sources = selector.css(".z--mb-16 .tec--badge::text").getall()

    categories = selector.css(".tec--badge--primary::text").getall()

    news["url"] = url
    news["title"] = title
    news["timestamp"] = timestamp
    news["writer"] = writer
    news["shares_count"] = int(shares_count)
    news["comments_count"] = int(comments_count)
    news["summary"] = "".join(summary)
    news["sources"] = [source.strip() for source in sources]
    news["categories"] = [category.strip() for category in categories]

    return news


# Requisito 5
def get_tech_news(amount):
    webpage = fetch("https://www.tecmundo.com.br/novidades")
    news = scrape_novidades(webpage)
    nextpage = scrape_next_page_link(webpage)
    tech_news = []

    while len(news) < amount:
        webpage = fetch(nextpage)
        news.extend(scrape_novidades(webpage))

    for url in news[:amount]:
        webpage = fetch(url)
        tech_news.append(scrape_noticia(webpage))

    create_news(tech_news)

    return tech_news
