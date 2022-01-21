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


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page_link = selector.css(
        "div.tec--list a.tec--btn::attr(href)"
    ).get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    return {url, title}


print(scrape_noticia(fetch("https://www.tecmundo.com.br/minha-serie/232000-7-servicos-voce-assistir-doramas-brasil.htm")))

# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
