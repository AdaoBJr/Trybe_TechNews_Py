import requests
import time
from parsel import Selector
from tech_news.database import create_news
import re

def fetch(url):
    response = ""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.exceptions.Timeout:
        return None
    finally:
        if response != "" and response.status_code == 200:
            return response.text
        else:
            return None


# Requisito 2
def scrape_novidades(html_content):
    select = Selector(text=html_content)
    card_title_link = select.css("h3.tec--card__title a::attr(href)").getall()
    if len(card_title_link) == 0:
        return []
    return card_title_link


# Requisito 3
def scrape_next_page_link(html_content):
    btn = "div.tec--list.tec--list--lg > a::attr(href)"
    select = Selector(text=html_content)
    next_page_link = select.css(btn).get()
    if next_page_link:
        return next_page_link
    return None


def shares_count_func(selector):
    answer = selector.css("div.tec--toolbar__item::text").get()
    if answer:
        answer = int(re.findall(r'\d+', answer)[0])
    else:
        answer = 0
    return answer 


# Requisito 4
def scrape_noticia(html_content):
    noticia = {}
    select = Selector(text=html_content)
    timestamp = "time#js-article-date::attr(datetime)"
    writer = "a.tec--author__info__link::text"
    writer2 = "div.tec--timestamp__item.z--font-bold > a::text"
    writer3 = "div > p.z--m-none.z--truncate.z--font-bold::text"
    comments_count = "button#js-comments-btn::attr(data-count)"
    sumary = ".tec--article__body > p:nth-child(1) *::text"
    categories = "div#js-categories a::text"
    sources = "div.z--mb-16.z--px-16 > div > a::text"
    sources2 = "div.z--mb-16 > div > a::text"
    title = "h1.tec--article__header__title::text"
    url = "link[rel=canonical]::attr(href)"
    select_shares_count = shares_count_func(select)
    select_writer = select.css(writer).get()
    select_source = select.css(sources).getall()

    if select_writer is not None:
        writer = select_writer
    else:
        writer = select.css(writer2).get()

    if select_source:
        sources = [sc.strip() for sc in select_source]
    else:
        sources = [source.strip() for source in select.css(sources2).getall()]

    if writer:
        writer = writer.strip()
    else:
        writer = select.css(writer3).get()

    noticia["title"] = select.css(title).get()
    noticia["timestamp"] = select.css(timestamp).get()
    noticia["writer"] = writer
    noticia["comments_count"] = int(select.css(comments_count).get())
    noticia["shares_count"] = int(select_shares_count)
    noticia["summary"] = "".join(select.css(sumary).getall())
    noticia["sources"] = sources
    noticia["categories"] = [
        category.strip() for category in select.css(categories).getall()
    ]
    noticia["url"] = select.css(url).get()

    return noticia


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
