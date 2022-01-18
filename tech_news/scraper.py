import requests
from time import sleep

# BASED ON *
# https://www.w3schools.com/python/ref_requests_get.asp
# https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
# https://github.com/tryber/sd-10b-live-lectures/blob/lecture/34.3/main_scraper.py
# *


# Requisito 1
def fetch(url):
    response = ""
    try:
        sleep(1)
        response = requests.get(url, timeout=3)

    except requests.exceptions.RequestException:
        pass

    finally:
        if response != "" and response.status_code == 200:
            return response.text
        pass


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
