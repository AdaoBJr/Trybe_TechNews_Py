from parsel import Selector
import requests
import time


URL = 'https://www.tecmundo.com.br/novidades'


def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    if not isinstance(html_content, str):
        return list()
    else:
        response = fetch(html_content)
        selector = Selector(text=response)
        links = selector.css('.tec--card__title a::attr(href)').getall()
        return links


def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    if not isinstance(html_content, str):
        return list()
    else:
        response = fetch(html_content)
        selector = Selector(text=response)
        next_page_link = selector.css('.tec--list > a::attr(href)').get()
        return next_page_link


if __name__ == "__main__":
    print(scrape_novidades({}))
