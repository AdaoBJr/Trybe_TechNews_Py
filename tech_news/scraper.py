import requests
import time
from parsel import Selector
from tech_news.database import create_news

# Requisito 1


def fetch(url):
    try:
        # recurso demora muito a responder
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            pass
    except requests.ReadTimeout:
        # Retornar none
        pass


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_link = selector.css(
        ".tec--list__item > article > div > h3 > a::attr(href)"
    ).getall()
    return news_link


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(".tec--btn::attr(href)").get()
    return next_page_link


# Requisito 4
def get_news_url(selector):
    return selector.css("head link[rel=canonical] ::attr(href)").get()


def get_news_title(selector):
    return selector.css(".tec--article__header__title ::text").get()


def get_news_timestamp(selector):
    # https://stackoverflow.com/questions/56427277/how-to-extract-the-value-of-the-datetime-attribute-in-a-time-tag-using-xpath-or
    return selector.css("time::attr(datetime)").get()


def get_news_writer(selector):
    css_class = [
        ".tec--author__info__link ::text",
        ".tec--timestamp a ::text",
        ".tec--author div .z--font-bold ::text",
    ]
    for item in css_class:
        writer = selector.css(item).get()
        if writer is not None:
            return writer.strip()


def get_news_share_count(selector):
    text_count = selector.css(".tec--toolbar div:nth-child(1)::text").get()
    if text_count is not None:
        return int(text_count.split(" ")[1])
    return 0


def get_news_comments_count(selector):
    text_count = selector.css("#js-comments-btn ::attr(data-count)").get()
    return int(text_count)


def get_news_summary(selector):
    TEXT = ""
    summary = TEXT.join(
        selector.css(".tec--article__body > p:nth-child(1) *::text").getall()
    )
    if summary is not None:
        return summary

    return None


def get_news_sources(selector):
    sources_list_dirty = selector.css(
        ".z--mb-16 div .tec--badge ::text"
    ).getall()
    sources_list_with_none = [source.strip() for source in sources_list_dirty]
    source_list = list(filter(None, sources_list_with_none))
    return source_list


def get_news_categories(selector):
    # https://www.delftstack.com/pt/howto/python/how-to-remove-whitespace-in-a-string/#:~:text=strip()%20M%C3%A9todo-,str.,e%20no%20fim%20da%20string.
    category_list_dirty = selector.css("#js-categories ::text").getall()
    category_list_with_none = [
        category.strip() for category in category_list_dirty
    ]
    category_list = list(filter(None, category_list_with_none))
    return category_list


def scrape_noticia(html_content):
    selector = Selector(html_content)
    news = {}
    news["url"] = get_news_url(selector)
    news["title"] = get_news_title(selector)
    news["timestamp"] = get_news_timestamp(selector)
    news["writer"] = get_news_writer(selector)
    news["shares_count"] = get_news_share_count(selector)
    news["comments_count"] = get_news_comments_count(selector)
    news["summary"] = get_news_summary(selector)
    news["sources"] = get_news_sources(selector)
    news["categories"] = get_news_categories(selector)
    return news


# Requisito 5
def get_tech_news(amount):
    ULR_BASE = "https://www.tecmundo.com.br/novidades"
    html = fetch(ULR_BASE)
    url_news_list = scrape_novidades(html)
    news_list = []
    while len(url_news_list) < amount:
        next_page_url = scrape_next_page_link(html)
        html = fetch(next_page_url)
        url_news_list.extend(scrape_novidades(html))
    for url_news in url_news_list:
        html_content = fetch(url_news)
        news = scrape_noticia(html_content)
        news_list.append(news)
    create_news(news_list)
    return news_list
