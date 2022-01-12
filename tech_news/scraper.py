import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    query_selector = "h3.tec--card__title a::attr(href)"
    allNotices = selector.css(query_selector).getall()
    return allNotices


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    query_selector = "a.tec--btn ::attr(href)"
    next_page_url = selector.css(query_selector).get()
    # Retorna None por padrão
    return next_page_url


def format_list_strip(list):
    list_formated = []
    for item in list:
        list_formated.append(item.strip())
    return list_formated


def format_shares_count(shares):
    if shares is not None:
        return int(shares.strip().split(" ")[0])
    return 0
# Requisito 4
# https://www.delftstack.com/pt/howto/python/how-to-remove-whitespace-in-a-string/#remover-espa%25C3%25A7os-em-branco-tanto-no-in%25C3%25ADcio-como-no-fim-de-uma-string-em-python
# https://python.wiki.br/python/como-concatenar-strings-em-python/


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    result = {
        "url": selector.css("head > meta:nth-child(28) ::attr(content)").get(),
        "title": selector.css("#js-article-title ::text").get(),
        "timestamp": selector.css(
            "div.tec--timestamp__item time ::attr(datetime)").get(),
        "writer": selector.css(".z--font-bold").css("*::text").get().strip()
        or "",
        "shares_count": format_shares_count(selector.css(
            ".tec--toolbar > div:nth-child(1)::text")
            .get()),
        "comments_count": int(selector.css(
            "#js-comments-btn::attr(data-count)").get()),
        "summary": "".join(selector.css(
            ".tec--article__body > p:nth-child(1) ::text").getall()),
        "sources": format_list_strip(selector.css(
            ".z--mb-16 .tec--badge ::text").getall()),
        "categories": format_list_strip(selector.css(
            "#js-categories a ::text").getall()),

    }
    print(result)
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
