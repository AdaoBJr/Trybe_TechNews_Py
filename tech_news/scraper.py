import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        res = requests.get(url, timeout=3)
    except requests.exceptions.RequestException:
        return None
    else:
        if res.status_code == 200:
            return res.text
    return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    return selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)

    return selector.css(".tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    # Zózimo, Arlen e Mari Mohr
    url_select = selector.css("link[rel=canonical]::attr(href)").get()

    title_select = selector.css(".tec--article__header__title::text").get()

    timestamp_select = selector.css("time::attr(datetime)").get()

    writer_select = selector.css(
        ".z--font-bold").css("*::text").get().strip() or ""

    try:
        shares_count = selector.css(
            ".tec--toolbar__item::text"
        ).get().strip().split(" ")[0]
    except AttributeError:
        shares_count = 0

    comments_count = selector.css(".tec--btn::attr(data-count)").get()

    summary_select = "".join(selector.css(
        ".tec--article__body > p:nth-child(1) ::text"
    ).getall())

    sources_select = selector.css(
        ".z--mb-16 .tec--badge::text"
    ).getall()

    categories_select = selector.css(
        ".tec--badge--primary::text"
    ).getall()

    return {
        "url": url_select,
        "title": title_select,
        "timestamp": timestamp_select,
        "writer": writer_select,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary_select,
        "sources": [source.strip() for source in sources_select],
        "categories": [category.strip() for category in categories_select],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    base_url = "https://www.tecmundo.com.br/novidades"
    fetch_url = fetch(base_url)
    notice_list = scrape_novidades(fetch_url)
    notice_result = []

    while len(notice_list) < amount:
        base_url = scrape_next_page_link(fetch_url)
        fetch_url = fetch(base_url)
        notice_list.extend(scrape_novidades(fetch_url))

    for notice_url in notice_list[0:amount]:
        data = fetch(notice_url)
        notice = scrape_noticia(data)
        notice_result.append(notice)

    create_news(notice_result)
    return notice_result
