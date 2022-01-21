from parsel import Selector
import time
import requests


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(f'\n{response.status_code}')
            return response.text
        else:
            print('else')
            return None
    except requests.Timeout:
        response = requests.Timeout
        print(response)
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    parentElement = selector.css("div.tec--list")
    links = parentElement.css(
        "a.tec--card__thumb__link::attr(href)"
    ).getall()
    return links


print(scrape_novidades(fetch("https://www.tecmundo.com.br/novidades")))


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
