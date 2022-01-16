from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    else:
        if response.status_code == 200:
            return response.text
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    titles = selector.css("h3.tec--card__title a::attr(href)").getall()
    return titles


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".tec--list .tec--btn::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# fetch("https://www.tecmundo.com.br/novidades")
# print(scrape_novidades(fetch("https://www.tecmundo.com.br/novidades")))
