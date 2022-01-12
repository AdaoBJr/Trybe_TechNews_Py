import requests
from parsel import Selector
from time import sleep
from tech_news.database import create_news


def retirar_espaco(lista):
    new_list = []
    for i in lista:
        if not i == " ":
            new_list.append(i.strip())

    return new_list


def check_string(valor):
    if valor is None:
        return None
    return valor.strip()


def check_comments(valor):
    if valor is None:
        return int(0)
    return int(valor)


def check_count(valor):
    if valor is None:
        return int(0)

    result = valor.strip().split(" ")[0]
    return int(result)


def check_writer(html_content):
    select = Selector(html_content)
    selectors = [
        "p.z--m-none.z--truncate.z--font-bold *::text",
        "div.tec--timestamp__item.z--font-bold > a ::text",
        "div.tec--article__body.p402_premium > p:nth-child(1) ::text",
    ]
    for selec in selectors:
        result = select.css(selec).get()
        if result is not None:
            return check_string(result)


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None

        return response.text
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    select = Selector(html_content)
    result = select.css("h3.tec--card__title > a::attr(href)").getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    select = Selector(html_content)
    result = select.css("div.tec--list.tec--list--lg > a::attr(href)").get()
    print(result)
    return result


# Requisito 4
def scrape_noticia(html_content):
    select = Selector(html_content)
    data = {}

    data["url"] = select.css("head > link[rel=canonical] ::attr(href)").get()
    data["title"] = select.css("#js-article-title ::text").get()
    data["timestamp"] = select.css("#js-article-date ::attr(datetime)").get()
    data["writer"] = check_writer(html_content)
    data["shares_count"] = check_count(
        select.css("nav.tec--toolbar > div::text").get()
    )
    data["comments_count"] = check_comments(
        select.css("#js-comments-btn ::attr(data-count)").get()
    )
    summary_list = select.css(
        "div.tec--article__body > p:nth-child(1) ::text"
    ).getall()
    data["summary"] = "".join(summary_list)
    data["sources"] = retirar_espaco(
        select.css("div.z--mb-16 > div > a ::text").getall()
    )
    data["categories"] = retirar_espaco(
        select.css("#js-categories *::text").getall()
    )
    return data


# Requisito 5
def get_tech_news(amount):
    if not isinstance(amount, int):
        return "Entrada invalida"

    lista_url_noticias = []
    screpe_fetch = fetch("https://www.tecmundo.com.br/novidades")
    lista_url_noticias += scrape_novidades(screpe_fetch)

    while len(lista_url_noticias) <= int(amount):
        next_url = scrape_next_page_link(screpe_fetch)
        next_page = fetch(next_url)
        lista_url_noticias += scrape_novidades(next_page)

    lista_dict_notice = []
    for x in range(amount):
        feth_noticia = fetch(lista_url_noticias[x])
        noticia = scrape_noticia(feth_noticia)
        lista_dict_notice.append(noticia)

    create_news(lista_dict_notice)

    return lista_dict_notice
