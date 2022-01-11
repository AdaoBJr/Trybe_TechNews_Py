import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=2)
        # response.raise_for_status() Não deu bom!
        # https://stackoverflow.com/questions/28377421/why-do-i-receive-a-timeout-error-from-pythons-requests-module
        if response.status_code == 200:
            return response.text
    except requests.exceptions.Timeout:
        return None
    # não entendi esse else, aula do Benites 10A
    # else:
    #     if response.status_code == 200:
    #         return response.text
    # return None


# Requisito 2
def scrape_novidades(html_content):
    # https://app.betrybe.com/course/computer-science/redes-e-raspagem-de-dados/raspagem-de-dados/ab38ab4e-bdbd-4984-8987-1abf32d85f26/conteudos/b63ffce8-be02-4be1-9b88-bda695400647/analisando-respostas/f8e39054-c9ab-49fb-aa02-4b4a26aa3323?use_case=side_bar
    selector = Selector(html_content)
    return selector.css(
        ".tec--list__item .tec--card__info h3 a::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(
        ".z--container .z--row .tec--list .tec--btn::attr(href)"
    ).get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
