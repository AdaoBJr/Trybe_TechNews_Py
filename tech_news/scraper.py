import requests
import time
from parsel import Selector


# Requisito 1
def fetch(URL):
    # A função deve receber uma URL
    res = ""
    try:
        # A função deve respeitar um Rate Limit de 1
        time.sleep(1)
        res = requests.get(URL, timeout=3)
        # A função deve fazer uma requisição
        # HTTP get para esta URL utilizando a função requests.get
    except requests.exceptions.Timeout:
        # "Timeout" e a função deve retornar None.
        return None
    finally:
        if res != "" and res.status_code == 200:
            # Status Code 200: OK, deve ser retornado seu conteúdo de texto;
            return res.text
        # status diferente de 200, deve-se retornar None
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    divlist = selector.css("div.tec--list__item")
    # Porque nao me permite usar direto o a.tec--card... Não sei??
    hreflist = divlist.css(
                """
                a.tec--card__title__link::attr(href)"""
                    ).getall()
    # print(hreflist)
    return hreflist


# Requisito 3
def scrape_next_page_link(html_content):
    # first_page = scrape_novidades(html_content)
    selector = Selector(text=html_content)
    next_page = selector.css("a.tec--btn::attr(href)").getall()
    if len(next_page) == 0:
        return None
    else:
        return next_page[0]
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
