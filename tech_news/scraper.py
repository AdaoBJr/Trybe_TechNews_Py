import requests
import time
import re
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
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
    selector = Selector(html_content)
    result = selector.css("div.tec--card__info h3 a::attr(href)").getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    result = selector.css("a.tec--btn::attr(href)").get()
    return result


def shares_count_func(selector):
    answer = selector.css("div.tec--toolbar__item::text").get()
    if answer:
        answer = re.findall(r'\d+', answer)[0]
    else:
        answer = 0
    return answer


# Requisito 4 [resolvido com ajuda da Letícia Galvão & Jonathan Souza]
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css(
        "div.tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = (
        selector.css(".z--font-bold").css("*::text").get().strip() or ""
    )
    shares_count = shares_count_func(selector)
    comments_count = selector.css(
        "button#js-comments-btn::attr(data-count)"
    ).get()

    get_summary = selector.css(
        "div.tec--article__body > p:nth-child(1) *::text"
    ).getall()
    summary = ''.join(get_summary)

    get_sources = selector.css("div.z--mb-16 div a::text").getall()
    sources = [i.strip() for i in get_sources]

    get_categories = selector.css("div#js-categories a::text").getall()
    categories = [i.strip() for i in get_categories]

    data = {}
    data["url"] = url
    data["title"] = title
    data["timestamp"] = timestamp
    data["writer"] = writer
    data["shares_count"] = int(shares_count)
    data["comments_count"] = int(comments_count)
    data["summary"] = summary
    data["sources"] = sources
    data["categories"] = categories

    return data


# Requisito 5
def get_tech_news(amount):
    fetch_url = fetch("https://www.tecmundo.com.br/novidades")
    novidades = scrape_novidades(fetch_url)
    next_page = scrape_next_page_link(fetch_url)

    while len(novidades) < amount:
        page = fetch(next_page)
        novidades += scrape_novidades(page)

    news = []
    for n in novidades[0:amount]:
        noticias = fetch(n)
        news.append(scrape_noticia(noticias))

    create_news(news)

    return news
