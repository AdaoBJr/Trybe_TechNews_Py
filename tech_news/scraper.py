import requests
import time

# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=2)
        # response.raise_for_status() Não deu bom!
        # https://stackoverflow.com/questions/28377421/why-do-i-receive-a-timeout-error-from-pythons-requests-module
        if response.status_code == 200:
            return response.text
    except requests.exceptions.Timeout:
        return None
    # não entendi esse else, aula do Benites 10A
    # else:
    #     if response.status_code == 200:
    #         return response.text
    # return None


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
