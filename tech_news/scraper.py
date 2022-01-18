import requests
import time
from tech_news.database import create_news
from parsel import Selector

# HELPER FUNCTIONS


def get_writer(selector):
    writer = selector.css(
        'a[href^="https://www.tecmundo.com.br/autor/"]::text'
    ).getall()
    if len(writer) > 1:
        return selector.css(
            'a[class][href^="https://www.tecmundo.com.br/autor/"]::text'
        ).get()
    try:
        return writer[0]
    except IndexError:
        return selector.css(".tec--author__info p::text").get()


def strip_list(list):
    stripped_list = []
    for item in list:
        stripped_list.append(item.strip())
    return stripped_list


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    else:
        if response.status_code == 200:
            return response.text
        else:
            return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news_hrefs = selector.css(".tec--card__info h3 a::attr(href)").getall()
    return news_hrefs


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page_href = selector.css(" .tec--btn::attr(href)").get()
    return next_page_href


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("meta[property='og:url']::attr(content)").get()

    title = selector.css(".tec--article__header__title::text").get()

    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    writer = get_writer(selector=selector)

    try:
        stripped_writer = writer.strip()
    except AttributeError:
        stripped_writer = writer

    shares_count = int(
        selector.css(".tec--toolbar__item::text").re_first(r"[0-9]") or "0"
    )
    comments_count = int(
        selector.css(".tec--toolbar__item button::attr(data-count)").get()
    )

    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()

    sources = selector.css(".z--mb-16 div a::text").getall()
    categories = selector.css("#js-categories a::text").getall()

    stripped_sources = strip_list(sources)
    stripped_categories = strip_list(categories)

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": stripped_writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": "".join(summary),
        "sources": stripped_sources,
        "categories": stripped_categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    base_url = "https://www.tecmundo.com.br/novidades"
    pages_to_scrape = []
    tech_news = []
    while base_url and len(tech_news) < amount:
        html_content = fetch(base_url)
        pages_to_scrape = scrape_novidades(html_content)
        for page in pages_to_scrape:
            page_content = fetch(page)
            page_info = scrape_noticia(page_content)
            tech_news.append(page_info)
        base_url = scrape_next_page_link(html_content=html_content)

    while len(tech_news) > amount:
        tech_news.pop()

    create_news(tech_news)
    return tech_news
