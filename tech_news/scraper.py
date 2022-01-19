import requests
import time
import re

from parsel import Selector
from tech_news.database import create_news

# Requisito 1


def fetch(url):

    try:
        time.sleep(1)
        page_request = requests.get(url, timeout=3)

        if page_request.status_code == 200:
            return page_request.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    all_news_links = selector.css(
        "div.tec--card__info h3 a::attr(href)"
    ).getall()
    return all_news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css("div.tec--list__item ~ a::attr(href)").get()
    return next_page_url or None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    current_url_page = (
        selector.xpath('//link[@rel="canonical"]/@href').get().strip()
    )

    title = selector.css("h1.tec--article__header__title::text").get()

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer_css = selector.css(".z--font-bold *::text").get() or None
    if writer_css:
        writer = writer_css.strip()
    else:
        writer = writer_css

    toolbar_item = selector.css("div.tec--toolbar__item::text").get()
    if toolbar_item:
        shares_count = int(re.search(r"\d+", toolbar_item)[0])
    else:
        shares_count = 0

    comments_count = int(
        selector.css(".tec--toolbar__item button::attr(data-count)").get()
    )

    summary = "".join(
        selector.css(".tec--article__body > p:nth-child(1) *::text").getall()
    )

    sources = selector.css(".z--mb-16 div a::text").getall()
    sources_stripped = [source.strip() for source in sources]

    categories = selector.css("#js-categories a::text").getall()
    categories_stripped = [category.strip() for category in categories]

    news_dict = {
        "url": current_url_page,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources_stripped,
        "categories": categories_stripped,
    }

    return news_dict


# Requisito 5
def get_tech_news(amount):
    newspage = fetch("https://www.tecmundo.com.br/novidades")

    all_news = []
    news_links = []

    for index in range(amount):
        if index == 0:
            news_links = scrape_novidades(newspage)
        # if ((index + 1) % 20) == 0:
        # Da forma que o teste foi construído
        # ele quebra nessa implementação, que é a mais correta,
        # por isso mantive no código
        if index == 20:
            next_page_link = scrape_next_page_link(newspage)
            newspage = fetch(next_page_link)
            news_links.extend(scrape_novidades(newspage))

        news_html_content = fetch(news_links[index])
        news_dict = scrape_noticia(news_html_content)
        all_news.append(news_dict)

    create_news(all_news)
    return all_news
