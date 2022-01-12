import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        r = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    else:
        if r.status_code != 200:
            return None
        return r.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    # agradecimentos ao Gabriel Essênio pela ajuda
    # na compreensão dos seletores na função css
    return selector.css(
        ".tec--list--lg .tec--card__title > a ::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    if html_content == "":
        return None

    selector = Selector(html_content)
    return selector.css(".tec--list--lg .tec--btn--primary::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    # selector = Selector(html_content)
    # url = selector.css('meta[property="og:url"]').attrib["content"]
    # title = selector.css("h1::text").get()
    # timestamp = selector.css("time::attr(datetime)").get()
    # writer = selector.css(".tec--author__info__link::text").get()
    """sources = [
        source.strip()
        for source in selector.css(".z--mb-16 > div > a::text").getall()
    ]"""
    """ categories = [
        category.strip()
        for category in selector.css("#js-categories a::text").getall()
    ] """
    # // a linha abaixo não funciona
    # summary = selector.css(".tec--article__body > p *::text").get()
    """ shares_count, comment_count = [
        int(social_num_info)
        for social_num_info in selector.css(".tec--toolbar__item *::text").re(
            r"\\d+"
        )
    ] """
    # print()
    # print(summary)
    # print({url, title})


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


""" with open("url.txt", "r") as reader:
    link_noticia = reader.readline()
    html_page_content = fetch(link_noticia)
    scrape_noticia(html_page_content) """
