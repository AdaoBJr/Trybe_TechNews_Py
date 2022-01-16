import requests
import time
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if not response.status_code == 200:
            return None
        return response.text
    except requests.Timeout:
        return None
# função que traz a pagina em html


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    lis = selector.css(
        ".tec--list--lg h3.tec--card__title a::attr(href)"
        ).getall()
    return lis
# acessando links do conteudo html


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link = selector.css(".tec--list.tec--list--lg > a ::attr(href)").get()
    return link
# acessando o link da proxima pagina


def write(selector):
    classes = [
        ".tec--timestamp__item.z--font-bold ::text",
        ".tec--author__info__link ::text",
        "div > p.z--m-none.z--truncate.z--font-bold::text",
    ]
    for item in classes:
        selected_class = selector.css(item).get()
        if selected_class is not None:
            return selected_class.strip()
    return None
# passando na lista de classes da pagina e tirando os espaços para criar o nome


def shares_count(selector):
    shares_count = selector.css(".tec--toolbar > div:nth-child(1)::text").get()
    if shares_count is not None:
        result = shares_count.strip().split(" ")[0]
        return int(result)
    return 0


def sources(selector):
    classes = [
        ".z--mb-16 > div > a ::text",
        ".z--mb-16.z--px-16 > div ::text",
    ]
    for item in classes:
        sources = selector.css(item).getall()
        if sources is not []:
            remove_spaces = list(map(lambda x: x.strip(), sources))
            return list(filter(lambda x: x != "", remove_spaces))
    return None
# map parecido com o js e o segundo parametro é onde vai


def categories(selector):
    categ = selector.css("#js-categories ::text").getall()
    remove_spaces = list(map(lambda x: x.strip(), categ))
    return list(filter(lambda x: x != "", remove_spaces))


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    obj = {}
    obj["url"] = selector.css("head > link[rel=canonical] ::attr(href)").get()
    # pegando o link do att rel e depois o herf
    obj["title"] = selector.css("#js-article-title ::text").get()
    obj["timestamp"] = selector.css("#js-article-date ::attr(datetime)").get()
    obj["writer"] = write(selector)
    obj["shares_count"] = shares_count(selector)
    obj["comments_count"] = int(
        selector.css("#js-comments-btn ::attr(data-count)").get()
    )
    obj["summary"] = "".join(
        selector.css(".tec--article__body > p:nth-child(1) *::text").getall()
    )
    obj["sources"] = sources(selector)
    obj["categories"] = categories(selector)
    return obj
# montando o obj desejado do req


# Requisito 5
def get_tech_news(amount):
    html_content = fetch("https://www.tecmundo.com.br/novidades")
    urls = scrape_novidades(html_content)

    newspaper = []

    while len(urls) < amount:
        next_page = scrape_next_page_link(html_content)
        html_content = fetch(next_page)
        urls.extend(scrape_novidades(html_content))
        # append de 1 em 1, extendo vários valores dentro de um array

    for index in range(amount):
        new_url = urls[index]
        page = fetch(new_url)
        info = scrape_noticia(page)
        newspaper.append(info)

    create_news(newspaper)

    return newspaper
# agradeço ao Pedro Henrique pela ajuda no projeto.
