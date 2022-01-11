import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(".z--container .tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    # feito com ajuda de Alessandra, Arlen e Mari
    selector = Selector(text=html_content)

    try:
        shares = int(
            "".join(
                filter(
                    str.isdigit,
                    selector.css(".tec--toolbar__item::text").getall()[0],
                )
            )
        )
    except IndexError:
        shares = 0
    try:
        comments = int(
            selector.css("#js-comments-btn::attr(data-count)").get()
        )
    except TypeError:
        comments = 0

    souces_list = selector.css(".z--mb-16 .tec--badge ::text").getall()
    categories_list = selector.css(".tec--badge--primary ::text").getall()
    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("time::attr(datetime)").get(),
        "writer": selector.css(".z--font-bold").css("*::text").get().strip()
        or "",
        "shares_count": shares,
        "comments_count": comments,
        "summary": "".join(
            selector.css(
                ".tec--article__body > p:nth-child(1) ::text"
            ).getall()
        ),
        "sources": [source.strip() for source in souces_list],
        "categories": [category.strip() for category in categories_list],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://www.tecmundo.com.br/novidades"
    response = fetch(url)
    news_list = scrape_novidades(response)
    news_result = []

    while len(news_list) < amount:
        url = scrape_next_page_link(response)
        response = fetch(url)
        news_list.extend(scrape_novidades(response))

    for notice in news_list[0:amount]:
        data = fetch(notice)
        news = scrape_noticia(data)
        news_result.append(news)

    create_news(news_result)
    return news_result
