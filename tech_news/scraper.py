import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        request = requests.get(url, timeout=1)
        if request.status_code != 200:
            return None
        return request.text
    except requests.Timeout:
        return None
    """Seu código deve vir aqui"""


# Requisito 2
# https://app.betrybe.com/course/computer-science/redes-e-raspagem-de-dados/raspagem-de-dados
# /ab38ab4e-bdbd-4984-8987-1abf32d85f26/conteudos/b63ffce8-be02-4be1-9b88-bda695400647/recursos-obtidos-a-partir-de-outro-recurso/45e6934f-7f20-41e4-bd56-e66f348c4685?use_case=side_bar
def scrape_novidades(html_content):
    selector = Selector(html_content)
    print(selector)
    return selector.css(".tec--list--lg h3 a::attr(href)").getall()
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    print(selector)
    return selector.css(".tec--list--lg > a::attr(href)").get()
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
