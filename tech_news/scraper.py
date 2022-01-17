import requests
import time
import parsel
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    get_element = parsel.Selector(html_content)

    return get_element.css(
        "div.tec--card__info > h3 > a ::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    get_element = (
        parsel.Selector(html_content).css(".tec--btn--lg::attr(href)").get()
    )
    return get_element


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    try:
        get_element = parsel.Selector(html_content)

        url = get_element.css("link[rel='canonical']::attr(href)").get()
        title = get_element.css(".tec--article__header__title::text").get()
        date = get_element.css("#js-article-date::attr(datetime)").get()
        write = get_element.css(".z--font-bold *::text").get().strip()
        counter_comments = get_element.css(".tec--btn::attr(data-count)").get()
        counter_share = (
            get_element.css(".tec--toolbar__item::text")
            .get()
            .lstrip()
            .split()[:2][0]
        )

    except AttributeError:
        counter_share = 0

    sumary = "".join(
        get_element.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )

    sources = get_element.css(".z--mb-16 .tec--badge::text").getall()

    categories = get_element.css("#js-categories > a::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": date,
        "writer": write,
        "shares_count": int(counter_share),
        "comments_count": int(counter_comments),
        "summary": sumary,
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url_fetch = fetch("https://www.tecmundo.com.br/novidades")
    url_news = scrape_novidades(url_fetch)

    while len(url_news) < amount:
        url_next = fetch(scrape_next_page_link(url_fetch))
        url_news.extend(scrape_novidades(url_next))

    news = []

    for url in url_news:
        url = scrape_noticia(fetch(url))
        if len(news) != amount:
            news.append(url)

    create_news(news)

    return news
