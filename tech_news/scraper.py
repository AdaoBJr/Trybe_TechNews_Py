import requests
import time
from parsel import Selector
import re
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    # A função deve receber uma URL

    res = ""
    try:
        # A função deve respeitar um Rate Limit de 1
        time.sleep(1)
        res = requests.get(url, timeout=3)
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
    # soup = BeautifulSoup(html_content, 'lxml')
    # URL OK
    url = scrapy_crazy.url_scrapy(selector)
    title = scrapy_crazy.title_scrapy(selector)
    timestamp = scrapy_crazy.timestamp_scrapy(selector)
    autor = scrapy_crazy.writer_scrapy(selector)
    contador_comentarios = scrapy_crazy.count_comment(selector)
    contador_compartilhamentos = scrapy_crazy.count_shares(selector)
    # summary = soup.find('div', {'class': "tec--article__body"})
    summary_text = scrapy_crazy.summary_text(selector)
    sources = scrapy_crazy.sources_text(selector)

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
    # categorias_html = soup.find('div', {'id': 'js-categories'})
    categorias = scrapy_crazy.categories_text(selector)
    # sources = []
    # for category in categorias_html:
    #     if category.text != '' and category.text != " ":
    #         categorias.append(category.text.strip())

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
        "timestamp": timestamp,
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
    url = "https://www.tecmundo.com.br/novidades"
    res = fetch(url)
    link_list = scrape_novidades(res)
    scrapy_results = []

    while len(link_list) < amount:
        url = scrape_next_page_link(res)
        res = fetch(url)
        # aqui também poderia ser usado o extend para adicionar no
        # final da lista
        link_list += scrape_novidades(res)

    # https://gist.github.com/RatulSaha/b41c52614da34762a74d16dc066b68df
    for notice_link in link_list[0:amount]:
        html = fetch(notice_link)
        scrapy_of_page = scrape_noticia(html)
        scrapy_results.append(scrapy_of_page)

    create_news(scrapy_results)
    return scrapy_results


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

    def writer_scrapy(selector):
        autor = selector.css(".z--font-bold").css("*::text").get().strip()

        return autor

    def count_comment(select):
        try:
            comentarios_html = select.css(
                "button.tec--btn::attr(data-count)").get()
            contador_comentarios = int(comentarios_html)
        except TypeError:
            contador_comentarios = 0

        return contador_comentarios

    def count_shares(select):
        try:
            contador_comentarios = select.css("div.tec--toolbar__item::text")
            contador_comentarios = re.findall(
                r"\d+", contador_comentarios.get())[0]
        except TypeError:
            contador_comentarios = '0'

        return int(contador_comentarios)

    def summary_text(select):
        summary = select.css(
            "div.tec--article__body > p:nth-child(1) *::text"
        ).getall()
        return "".join(summary)

    def sources_text(select):
        sources = select.css(
            "div.z--mb-16 > div > a.tec--badge::text").getall()

        return [source.strip() for source in sources]

    def categories_text(select):
        categories = select.css("div#js-categories > a::text").getall()

        return [category.strip() for category in categories]
