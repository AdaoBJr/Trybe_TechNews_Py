from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if not response.status_code == 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("h3.tec--card__title > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("div.tec--list > a::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news = {}
    news["url"] = selector.css("head > link[rel=amphtml]::attr(href)").get()
    news["title"] = selector.css("h1.tec--article__header__title::text").get()
    news["timestamp"] = selector.css(
        "div.tec--timestamp__item > time::attr(datetime)"
    ).get()
    news["writer"] = selector.css(".tec--author__info__link::text").get()
    news["shares_count"] = (
        selector.css("div.tec--toolbar__item::text")
        .get()
        .strip()
        .split(" ")[0]
    )
    news["comments_count"] = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()
    news["summary"] = "".join(
        selector.css(".tec--article__body > p:nth-child(1)::text").getall()
    )
    news["categories"] = selector.css(
        "a.tec--badge.tec--badge--primary::text"
    ).getall()

    print("*\n ****************** \n", news, "*********************")
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
