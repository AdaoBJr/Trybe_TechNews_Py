import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        res = requests.get(url, timeout=3)
        if res.status_code != 200:
            return None
        return res.text
    except requests.Timeout:
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_novidades(html_content):
    sel = Selector(text=html_content)
    link = ".tec--list h3 a::attr(href)"
    return sel.css(link).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    sel = Selector(text=html_content)
    return sel.css(".tec--list--lg .tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


print(fetch("https://www.tecmundo.com.br/novidades/"))
print(scrape_novidades("https://www.tecmundo.com.br/novidades/"))
print(scrape_next_page_link("https://www.tecmundo.com.br/novidades/"))
