import requests
import time


# Requisito 1
def fetch(url):
    try:
        # fazendo uma requisição e esperando no max 3 seg
        time.sleep(1)
        res = requests.get(url, timeout=2)
    except requests.exceptions.RequestException:
        return None
    else:
        # Testabdo se a comunicação com o site está ok, retorna o texto
        if res.status_code == 200:
            return res.text
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
