import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            response.raise_for_status()
        return response.text

    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    val = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()
    return val


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    val = selector.css(".tec--list .tec--btn::attr(href)").get()
    return val


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()

    writer = selector.css(".z--font-bold  *::text").get() or None
    if writer:
        writer = writer.strip()

    shares_count = (
        selector.css(".tec--toolbar .tec--toolbar__item").css("::text").get()
    )

    try:
        shares_count = shares_count.strip().split(" ")[0]
        shares_count = int(shares_count)
    except Exception:
        shares_count = 0

    comments_count = selector.css(".tec--btn::attr(data-count)").get() or 0
    comments_count = int(comments_count)

    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    summary = "".join(summary)

    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories .tec--badge::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": [x.strip() for x in sources],
        "categories": [x.strip() for x in categories],
    }


# Requisito 5
def get_tech_news(amount):
    scrapping_url = "https://www.tecmundo.com.br/novidades"
    news_url_list = []
    scrapped_news = []

    while len(news_url_list) < amount:
        news_content = fetch(scrapping_url)
        news_urls = scrape_novidades(news_content)
        news_url_list.extend(news_urls)
        scrapping_url = scrape_next_page_link(news_content)

    for link in news_url_list[0:amount]:
        page = fetch(link)
        scrapped = scrape_noticia(page)
        scrapped_news.append(scrapped)

    create_news(scrapped_news)
    return scrapped_news
