import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None        
    if response.status_code == 200:
        return response.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    url = selector.css(
        ".tec--list__item  .tec--card__title__link::attr(href)"
    ).getall()
    return url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--btn.tec--btn--lg"
        ".tec--btn--primary.z--mx-auto.z--mt-48::attr(href)"
    ).get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url_selected = (
        selector.css('meta[property="og:url"]::attr("content")').get()
    )
    title_selected = selector.css(".tec--article__header__title::text").get()
    timestamp_selected = selector.css("time::attr(datetime)").get()
    writer_selected = (
        selector.css(".z--font-bold").css("*::text").get().strip() or ""
    )
    try:
        shares_count = (
            selector.css(".tec--toolbar__item::text")
            .get()
            .strip()
            .split(" ")[0]
        )
    except AttributeError:
        shares_count = 0
        
    comments_count = selector.css(".tec--btn::attr(data-count)").get()
    summary_selected = "".join(
        selector.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )
    sources_selected = selector.css(".z--mb-16 > div > a::text").getall()
    categories_selected = selector.css("div#js-categories a::text").getall()

    return {
        "url": url_selected,
        "title": title_selected,
        "timestamp": timestamp_selected,
        "writer": writer_selected,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary_selected,
        "sources": [source.strip() for source in sources_selected],
        "categories": [category.strip() for category in categories_selected],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
