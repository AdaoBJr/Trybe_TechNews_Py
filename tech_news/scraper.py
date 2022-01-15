import time
from requests import get


# Requisito 1

def fetch(url):
    time.sleep(1)
    STATUS_OK = 200
    try:
        response = get(url, headers={"Accept": "text/html"}, timeout=3)
        return response.text if response.status_code == STATUS_OK else None
    except Exception:
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
