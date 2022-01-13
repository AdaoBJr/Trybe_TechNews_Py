from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        # https://docs.python-requests.org/en/latest/user/advanced/#timeouts
        response.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    novidades = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()

    return novidades


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_button_link = selector.css(".tec--btn::attr(href)").get()

    return next_page_button_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title ::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get() or ""

    try:
        shares_count = (
            selector.css(".tec--toolbar__item::text")
            .get()
            .strip()
            .split(" ")[0]
        )
    except AttributeError:
        shares_count = 0

    comments_count = (
        selector.css("#js-comments-btn ::text").getall()[1].split()[0]
    )

    summary = "".join(
        selector.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )

    sources = selector.css(".z--mb-16 .tec--badge ::text").getall()
    categories = selector.css(".tec--badge--primary ::text").getall()

    news_dict = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip(),
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }

    return news_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    pass
