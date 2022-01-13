import requests
import time
import parsel


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        # https://docs.python-requests.org/en/latest/user/advanced/#timeouts
        response.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    novidades = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()

    return novidades


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
