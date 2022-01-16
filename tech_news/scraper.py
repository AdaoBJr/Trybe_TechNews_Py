import requests
import time
from parsel import Selector
from tech_news.database import create_news


"""Requisito 4 feito com a ajuda do Eder Paiva e do Jonathan Souza"""
"""Requisito 5 com ajuda dos colegas Cristian Bugs e Eder Paiva """


def url_results(selector):
    link = selector.css(
        "link[rel=canonical]::attr(href)"
        ).get()
    return link


def title_results(selector):
    title = selector.css(
        "h1.tec--article__header__title::text"
        ).get()
    return title


def timestamp_results(selector):
    timestamp = selector.css(
        "div.tec--timestamp__item time::attr(datetime)"
        ).get()
    return timestamp


def writer_results(selector):
    writer = selector.css(
        "a.tec--author__info__link::text"
        ).get()
    if writer is None:
        writer = selector.css(
            "div.tec--timestamp div:nth-child(2) a::text").get()
        if writer is None:
            writer = selector.css("p.z--m-none::text").get()
    return writer.strip()


def shares_count_results(selector):
    shares_count = selector.css(
        "div.tec--toolbar__item::text"
        ).get()
    """ Vai pegar somente os numeros(string) e transformar em um INT """
    if shares_count:
        shares_count = shares_count.replace('Compartilharam', '')
        shares_count = int(shares_count.strip())
    else:
        shares_count = 0
    return shares_count


def comment_count_results(selector):
    comment_count = selector.css(
        "button.tec--btn::attr(data-count)"
        ).get()
    return int(comment_count)


def summary_results(selector):
    summary = selector.css(
        "div.tec--article__body > p:nth-child(1) *::text"
        ).getall()
    return "".join(summary)


def sources_results(selector):
    sources = selector.css(
        "div.z--mb-16 > div > a.tec--badge::text"
        ).getall()
    """ retira os espaços desnecessarios e faz um for nas fontes """
    return [source.strip() for source in sources]


def categories_results(selector):
    categories = selector.css(
        "div#js-categories a::text"
        ).getall()

    return [category.strip() for category in categories]


# Requisito 1
def fetch(url):
    try:
        """ Uma requisição por segundo e com resposta até no max 3s """
        time.sleep(1)
        res = requests.get(url, timeout=3)
        res.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    else:
        return res.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    result = selector.css(
        ".tec--list.tec--list--lg h3 > a ::attr(href)"
        ).getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    result = selector.css(
        ".tec--list.tec--list--lg > a::attr(href)"
        ).get()
    return result


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    link = url_results(selector)
    title = title_results(selector)
    timestamp = timestamp_results(selector)
    writer = writer_results(selector)
    shares_count = shares_count_results(selector)
    comments = comment_count_results(selector)
    summary = summary_results(selector)
    sources = sources_results(selector)
    category = categories_results(selector)

    """ criar o objeto para armazenar as informaçções """
    obj_news = {}

    """atribuir as chaves e valor relacionadas as informações das função aux"""
    obj_news["url"] = link
    obj_news["title"] = title
    obj_news["timestamp"] = timestamp
    obj_news["writer"] = writer
    obj_news["shares_count"] = shares_count
    obj_news["comments_count"] = comments
    obj_news["summary"] = summary
    obj_news["sources"] = sources
    obj_news["categories"] = category

    return obj_news


# Requisito 5
def get_tech_news(amount):
    link = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(link)
    novidades = scrape_novidades(html_content)

    while len(novidades) < amount:
        scrap_link_next_page = scrape_next_page_link(html_content)
        html_content = fetch(scrap_link_next_page)
        novidades += scrape_novidades(html_content)

    noticias = []
    """ comeca com i = 0 e vai até o valor de amount """
    for i in range(amount):
        """ vou pegar todos os links da minha lista """
        link_noticias = novidades[i]
        html_content = fetch(link_noticias)
        noticias += [scrape_noticia(html_content)]

    create_news(noticias)
    return noticias
