# VQV
import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
    except requests.Timeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    # https://advertools.readthedocs.io/en/master/_modules/advertools/spider.html
    # https://app.betrybe.com/course/computer-science/redes-e-raspagem-de-dados/raspagem-de-dados/ab38ab4e-bdbd-4984-8987-1abf32d85f26/conteudos/b63ffce8-be02-4be1-9b88-bda695400647/analisando-respostas/f8e39054-c9ab-49fb-aa02-4b4a26aa3323?use_case=side_bar
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    # Referência de ideia de seleção pela fonte, não do código em si.
    # https://github.com/tryber/sd-09-tech-news/pull/4/commits/525d9240d1a87cb8e1a3c437b5ffca38ba0db345
    writer = selector.css(".z--font-bold *::text").get()
    writer = writer.strip() if writer else None
    shares_count = selector.css(".tec--toolbar__item::text").get()
    s_count = int(shares_count.strip().split(" ")[0]) if shares_count else 0
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    comments_count = int(comments_count) if comments_count else 0
    summary = "".join(
        selector.css(".tec--article__body > p:first-of-type *::text").getall()
    ).strip()
    sources = [
        source.strip()
        for source in selector.css(".z--mb-16 div .tec--badge::text").getall()
    ]
    categories = [
        category.strip()
        for category in selector.css("#js-categories a::text").getall()
    ]
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": s_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

# html = fetch(url)
# scrape = scrape_noticia(html)
# print(scrape)


# Requisito 3
# como define a partir de qual ponto da sequencia de divs o selector pega?
# Porque "h3.tec--card__title .tec--card__title__link::attr(href)" e não
# ".tec--card__title__link::attrf(href)" ou
# "tec--card__title .tec--card__title__link::attr(href) ?"
# R: o selector.css recupera o atributo href do primeiro elemento que combine
# com todo o seletor
# get all estava retornando muitos links?
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links = selector.css(
        ".tec--list__item .tec--card__thumb > a:first-of-type::attr(href)"
    ).getall()
    return links if links else []


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css(
        ".tec--list--lg .tec--btn--primary::attr(href)"
    ).get()
    return next_page_url
# url = "https://www.tecmundo.com.br/novidades"
# html = fetch(url)
# scrape_next_page = scrape_next_page_link(html)
# print(scrape_next_page)


# Requisito 5
def get_tech_news(amount):
    news = []
    url = "https://www.tecmundo.com.br/novidades"
    counter = 0
    while counter < amount:
        news_page_content = fetch(url)
        news_url_in_page = scrape_novidades(news_page_content)
        for url in news_url_in_page:
            html_content = fetch(url)
            data = scrape_noticia(html_content)
            news.append(data)
            counter += 1
            if counter == amount:
                break
        url = scrape_next_page_link(news_page_content)
    create_news(news)
    return news


# get_tech_news(10)