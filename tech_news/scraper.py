import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        # fazendo uma requisição e esperando no max 3 seg
        time.sleep(1)
        res = requests.get(url, timeout=3)
    except requests.exceptions.RequestException:
        return None
    else:
        # Testabdo se a comunicação com o site está ok, retorna o texto
        if res.status_code == 200:
            return res.text
    return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    # faz a busca no arquivo pela classe css,
    # encontrando a div e depois disso a tag q possui o atr href
    result = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    # faz a busca no arquivo pela classe css,
    # encontrando o pai e depois disso a tag q possui o atr href
    result = selector.css(".tec--btn::attr(href)").get()
    return result


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    # zozimo, arlen e alessandra
    url = selector.css("link[rel=canonical] ::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("time ::attr(datetime)").get()
    writer = selector.css(
        ".z--font-bold").css("*::text").get().strip() or " "

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
    sources = selector.css(".z--mb-16 .tec--badge ::text").getall()

    categories = selector.css(".tec--badge--primary::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary_select,
        "sources": [source.strip() for source in sources],
        "categories": [categories.strip() for categories in categories],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
