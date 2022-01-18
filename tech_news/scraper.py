import requests
import time
import parsel
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        result = requests.get(url, timeout=3)
        if result.status_code == 200:
            return result.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    return selector.css("h3.tec--card__title > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    return selector.css("div.tec--list.tec--list--lg > a::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    # url, title, timestamp (da noticia),
    # writer, shares_count, comments_count,
    # summary, sources, catergories
    selector = parsel.Selector(html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title ::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn ::attr(data-count)").get()
    summary = selector.css(
        ".tec--article__body > p:nth-child(1) ::text"
        ).getall()
    sources = selector.css(".z--mb-16 .tec--badge ::text").getall()
    categories = selector.css("#js-categories a::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip() if writer else None,
        "shares_count": int(shares_count.split()[0]) if shares_count else 0,
        "comments_count": int(comments_count) if comments_count else 0,
        "summary": "".join(summary),
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://www.tecmundo.com.br/novidades"
    fetch_url = fetch(url)
    news_list = []

    while len(news_list) < amount:
        for url in scrape_novidades(fetch_url):
            if len(news_list) < amount:
                news_fetch = fetch(url)
                news_list.append(scrape_noticia(news_fetch))

        if len(news_list) < amount:
            url = scrape_next_page_link(fetch_url)
            fetch_url = fetch(url)

    create_news(news_list)
    return news_list
