import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup
# from tech_news.database import create_news


# Requisito 1
def fetch(URL):
    # A função deve receber uma URL

    res = ""
    try:
        # A função deve respeitar um Rate Limit de 1
        time.sleep(1)
        res = requests.get(URL, timeout=3)
        # A função deve fazer uma requisição
        # HTTP get para esta URL utilizando a função requests.get
    except requests.exceptions.Timeout:
        # "Timeout" e a função deve retornar None.
        return None
    finally:
        if res != "" and res.status_code == 200:
            # Status Code 200: OK, deve ser retornado seu conteúdo de texto;
            return res.text
        # status diferente de 200, deve-se retornar Non
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    divlist = selector.css("div.tec--list__item")
    # Porque nao me permite usar direto o a.tec--card... Não sei??
    hreflist = divlist.css(
                """
                a.tec--card__title__link::attr(href)"""
                    ).getall()
    # print(hreflist)
    return hreflist


# Requisito 3
def scrape_next_page_link(html_content):
    # first_page = scrape_novidades(html_content)
    selector = Selector(text=html_content)
    next_page = selector.css("a.tec--btn::attr(href)").getall()
    if len(next_page) == 0:
        return None
    else:
        return next_page[0]
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    soup = BeautifulSoup(html_content, 'lxml')
    # URL OK
    url = scrapy_crazy.url_scrapy(selector)
    title = scrapy_crazy.title_scrapy(selector)
    timestamp = scrapy_crazy.timestamp_scrapy(selector)
    autor = scrapy_crazy.writer_scrapy(soup)
    contador_comentarios = scrapy_crazy.count_comment(soup)
    contador_compartilhamentos = scrapy_crazy.count_shares(soup)
    summary = soup.find('div', {'class': "tec--article__body"})
    summary_text = summary.contents[0].text
    sources = scrapy_crazy.sources_text(soup)

    # print(summary.text, "estou aqui")
    # fontes = selector.css("div.z--mb-16 div a::text").getall()
    # fontes = soup.find("h2", {
    #     'class': [
    #         "z--text-base",
    #         "z--font-semibold",
    #         "z--mt-none",
    #         "z--mb-8"]}).next_sibling.contents
    # # verificar se fontes existem!!
    # fonte_exists = soup.find_all("h2", {
    #     'class': [
    #         "z--text-base",
    #         "z--font-semibold",
    #         "z--mt-none",
    #         "z--mb-8"]})

    # preciso pegar o filho com id, depois fazer o for!
    categorias_html = soup.find('div', {'id': 'js-categories'})
    categorias = []
    # sources = []
    for category in categorias_html:
        if category.text != '' and category.text != " ":
            categorias.append(category.text.strip())

    # for fonte in fontes:
    #     if fonte != '' and fonte != " ":
    #         sources.append(fonte.strip())

    # for fonte in fontes:
    #     if fonte != '' and fonte != " ":
    #         sources.append(fonte.text.strip())

    # print(fonte_exists[0].text)
    # if fonte_exists[0].text != 'Fontes':
    #     sources = []

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp["datetime"],
        "writer": autor,
        "shares_count": contador_compartilhamentos,
        "comments_count": contador_comentarios,
        "summary": summary_text,
        "sources": sources,
        "categories": categorias
    }
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    pass


class scrapy_crazy:
    # primeira refatoração para select pra ver se erro e bs4
    def url_scrapy(selector):
        url = selector.css("link[rel=canonical]::attr(href)").get()
        return url

    def title_scrapy(selector):
        # segunda refatoração para select pra ver se erro e bs4
        title = selector.css("h1.tec--article__header__title::text").get()
        return title

    def timestamp_scrapy(selector):
        # terceira refatoração para select pra ver se erro e bs4
        timestamp = selector.css("time::attr(datetime)").get()
        return timestamp

    def writer_scrapy(soup):
        try:
            autorhtml = soup.find('a', attrs={
                'class': "tec--author__info__link"}).text.strip()
        except AttributeError:
            try:
                autorhtml = soup.find('div', attrs={
                    'class': "tec--timestamp"}).contents[1].text.strip()
            except IndexError:
                autorhtml = soup.find('p', attrs={
                    'class': "z--m-none"}).text.strip()

        return autorhtml

    def count_comment(soup):
        comentarios_html = soup.find('button', attrs={
            'id': "js-comments-btn"
        })
        contador_comentarios = int(comentarios_html["data-count"])

        return contador_comentarios

    def count_shares(soup):
        compartilharam_html = soup.find_all('div', attrs={
            'class': "tec--toolbar__item"})[0].text
    # print(compartilharam_html)
        compartilhamentos = compartilharam_html.replace("Compartilharam", "")
        compartilhamentos = compartilhamentos.replace("Comentários", "")

        return int(compartilhamentos)

    def summary_text(soup):
        summary = soup.find(True, {
            'class': ["tec--article__body", "z--px-16", "p402_premium"]})
        summary_text = summary.contents[0].text
        # print(summary_text, " class here ")
        return summary_text

    def sources_text(soup):
        sources = []
        fontes = soup.find("h2", {
            'class': [
                "z--text-base",
                "z--font-semibold",
                "z--mt-none",
                "z--mb-8"]}).next_sibling.contents
    # verificar se fontes existem!!
        fonte_exists = soup.find_all("h2", {
            'class': [
                "z--text-base",
                "z--font-semibold",
                "z--mt-none",
                "z--mb-8"]})

        for fonte in fontes:
            if fonte != '' and fonte != " ":
                sources.append(fonte.text.strip())

        if fonte_exists[0].text != 'Fontes':
            sources = []

        return sources
