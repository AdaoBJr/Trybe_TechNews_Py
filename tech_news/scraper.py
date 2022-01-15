from parsel import Selector
from tech_news.database import create_news
import time
import requests

regex_number = r"\d+"
selector_url = "head > link[rel=canonical]::attr(href)"
selector_title = "h1.tec--article__header__title::text"
selector_timestamp = "div.tec--timestamp__item > time::attr(datetime)"
selector_writer = ".z--font-bold"
selector_shares_count = ".tec--toolbar > .tec--toolbar__item::text"
selector_comments_count = ".tec--toolbar__item > button::attr(data-count)"
selector_sumary = ".tec--article__body > p:nth-child(1) *::text"
selector_sources = ".z--mb-16 div a::text"
selector_categories = "#js-categories a::text"


# Requisito 1
def fetch(url):
    time.sleep(5)

    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None

    if(response.status_code == 200):
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news = selector.css("div.tec--list")
    news_links = news.css(
        "figure a.tec--card__thumb__link::attr(href)"
    ).getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    page_link = selector.css("div.tec--list > a.tec--btn::attr(href)").get()
    return page_link


def rm_spaces_in_array(array):
    result = []
    for string in array:
        result.append(string[1:-1])
    return result


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css(selector_url).get()
    title = selector.css(selector_title).get()
    timestamp = selector.css(selector_timestamp).get()
    writer = (
        selector.css(selector_writer).css("*::text").get().strip() or ""
    )
    shares_count = int(
        selector.css(selector_shares_count).re_first(regex_number) or 0
    )
    comments_count = int(selector.css(selector_comments_count).get() or 0)
    summary = "".join(selector.css(selector_sumary).getall())
    sources = rm_spaces_in_array(selector.css(selector_sources).getall())
    categories = rm_spaces_in_array(selector.css(selector_categories).getall())
    return{
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'shares_count': shares_count,
        'comments_count': comments_count,
        'summary': summary,
        'sources': sources,
        'categories': categories
    }


# Requisito 5
def get_tech_news(amount):
    page_html = fetch("https://www.tecmundo.com.br/novidades")
    news_links = []
    result_news_scraped = []

    news_links.extend(scrape_novidades(page_html))

    counter = 0
    while counter < amount:
        page_news_html = {}

        try:
            page_news_html = fetch(news_links[counter])
        except IndexError:
            page_link = scrape_next_page_link(page_html)
            page_html = fetch(page_link)
            news_links.extend(scrape_novidades(page_html))
            page_news_html = fetch(news_links[counter])

        result_news_scraped.append(scrape_noticia(page_news_html))
        # print(f"OBJETO {counter}:::", news_scraped[counter], "\n")
        counter += 1

    create_news(result_news_scraped)
    return result_news_scraped


# get_tech_news(10)
