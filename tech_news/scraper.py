import requests
from time import sleep


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        res = requests.get(url, timeout=3)
        if res.status_code != 200:
            return None
        else:
            return res.text
    except requests.Timeout:
        return None


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
