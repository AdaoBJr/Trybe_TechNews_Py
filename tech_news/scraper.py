import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    else:
        return response.text


print(fetch("https://www.tecmundo.com.br/novidades"))


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui

    selector = parsel.Selector(param)
    quotes = []
    for quotes in selector.css('div.quote')
    text = quote.css('div.txt').get()
    author = quote.css('div.author').get()
    tags = quote.css('div.tags').getall()
    quotes.append({
        "text": text
        "author": author
        "tags": tags
    })

    return quotes


    """
    pass


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    pass


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    pass


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    pass
