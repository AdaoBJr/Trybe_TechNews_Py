from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
# response.raise_for_status() ->
# retorna um objeto HTTPError se ocorrer um erro durante o processo
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    else:
        return response.text


# Requisito 2
# getAll -> Para extrair os dados textuais
# retorna uma lista com todos os resultados
def scrape_novidades(html_content):
    if html_content == '':
        return []
    return Selector(html_content).css(
        'h3 .tec--card__title__link::attr(href)').getall()


# Requisito 3
# ::attr(href) -> href referencia para navegação
# get elemento
def scrape_next_page_link(html_content):
    selec = Selector(html_content)
    return selec.css(".tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    if html_content == "":
        return []

    selector = Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    escritor = selector.css(".z--font-bold *::text").get().strip()
    comentario = selector.css(".tec--toolbar__item::text").get()

    if comentario:
        shares = comentario.split()[0]
    else:
        shares = 0

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    sum = selector.css(".tec--article__body > p:nth-child(1) *::text").getall()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    source = [i.strip() for i in sources]
    categories = selector.css("#js-categories a::text").getall()
    category = [i.strip() for i in categories]

    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': escritor,
        'shares_count': int(shares),
        'comments_count': int(comments_count),
        'summary': "".join(sum),
        "sources": source,
        "categories": category,
    }


# Requisito 5
def get_tech_news(amount):
    url_fetch = fetch("https://www.tecmundo.com.br/novidades")
    url_news = scrape_novidades(url_fetch)

    while len(url_news) < amount:
        url_next = fetch(scrape_next_page_link(url_fetch))
        url_news.extend(scrape_novidades(url_next))

    news = []

    for url in url_news:
        url = scrape_noticia(fetch(url))
        if len(news) < amount:
            news.append(url)

    create_news(news)

    return news
