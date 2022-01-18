import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    if html_content == "":
        return []
    seletor = Selector(html_content)
    card_title = seletor.css("h3 .tec--card__title__link::attr(href)").getall()
    return card_title


# Requisito 3
def scrape_next_page_link(html_content):
    seletor = Selector(html_content)
    next_page = seletor.css(
        "div.tec--list--lg a.tec--btn--lg::attr(href)"
    ).get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    seletor = Selector(html_content)
    # https://rockcontent.com/br/blog/canonical-tag/
    url = seletor.css("link[rel=canonical]::attr(href)").get()
    title = seletor.css(".tec--article__header__title::text").get()
    timestamp = seletor.css("time::attr(datetime)").get()
    writer = seletor.css(".z--font-bold").css("*::text").get().strip() or ""
    shares_count = seletor.css("div.tec--toolbar__item::text").get()
    if shares_count:
        shares_count = shares_count.replace("Compartilharam", "").strip()
    else:
        shares_count = 0
    comments_count = seletor.css(".tec--btn::attr(data-count)").get()
    summary = "".join(
        seletor.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )
    sources = seletor.css(".z--mb-16 .tec--badge::text").getall()
    categories = seletor.css(".tec--badge--primary::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(url)
    news = scrape_novidades(html_content)
    news_list = []

    while len(news) < amount:
        url = scrape_next_page_link(html_content)
        html_content = fetch(url)
        news.extend(scrape_novidades(html_content))

    for new_url in news[0:amount]:
        response = fetch(new_url)
        new = scrape_noticia(response)
        news_list.append(new)

    create_news(news_list)
    return news_list
