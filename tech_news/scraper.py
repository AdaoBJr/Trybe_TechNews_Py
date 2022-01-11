import requests
from parser import Selector


# Requisito 1
def fetch(url):
    try:
        res = requests.get(url, timeout=3)
        res.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    finally:
        if res.status_code != 200:
            return None
        else:
            return res.text


# Requisito 2
def scrape_novidades(html_content):
    url = "https://www.tecmundo.com.br/novidades"
    res = requests.get(html_content)
    selector = Selector(text=res.text)
    links = []
    news_list = selector.css("div:nth-child(1) > article > div > h3 > a")
    try:
        for link in news_list:
            path = link.attrib["href"]
            links.append(f"{url}{path}")
    except KeyError:
        return []

    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    print(html_content)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
