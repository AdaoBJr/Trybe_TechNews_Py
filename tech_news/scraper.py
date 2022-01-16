import requests
import time


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    response = requests.get(url)
    return response.content


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


fetch("https://www.tecmundo.com.br/novidades")
