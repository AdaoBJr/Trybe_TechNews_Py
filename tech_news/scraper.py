import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    result = selector.xpath(
        "/html/body/div/main/div/div/div/div/div/article/div/h3/a/@href"
    ).getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    result = selector.xpath("/html/body/div/main/div/div/div/div/a/@href").get()
    return result


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    base_url = "https://www.tecmundo.com.br/novidades"
    fetch_url = fetch(base_url)
    novidades_urls = scrape_novidades(fetch_url)
    print(novidades_urls)
