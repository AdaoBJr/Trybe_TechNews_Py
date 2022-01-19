import requests
import time


# Requisito 1

def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, timeout=3)
        res.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    return res.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    get_all = Selector(html_content).xpath(
      "/html/body/div/main/div/div/div/div/div/article/div/h3/a/@href"
    )
    return get_all


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
