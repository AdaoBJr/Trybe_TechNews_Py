import requests
import time
from parsel import Selector
from tech_news.database import create_news

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
    # https://app.betrybe.com/course/computer-science/redes-e-raspagem-de-dados/raspagem-de-dados/ab38ab4e-bdbd-4984-8987-1abf32d85f26/conteudos/b63ffce8-be02-4be1-9b88-bda695400647/analisando-respostas/f8e39054-c9ab-49fb-aa02-4b4a26aa3323?use_case=side_bar
    selector = Selector(html_content)
    return selector.css(
        ".tec--list__item .tec--card__info h3 a::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(
        ".z--container .z--row .tec--list .tec--btn::attr(href)"
    ).get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url_selector = selector.css("link[rel=canonical]::attr(href)").get()

    title_selector = selector.css(".tec--article__header__title::text").get()

    timestamp_selector = selector.css("time::attr(datetime)").get()

    # o método strip remove espeços em branco no início e fim de uma string
    writer_selector = (
        selector.css(".z--font-bold").css("*::text").get().strip() or ""
    )

    # https://github.com/tryber/sd-010-b-tech-news/pull/10/files
    try:
        shares_count = (
            selector.css(".tec--toolbar__item::text")
            .get()
            .strip()
            .split(" ")[0]
        )
    except AttributeError:
        shares_count = 0

    comments_count = selector.css(".tec--btn::attr(data-count)").get()

    summary_selector = "".join(
        selector.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )

    sources_selector = selector.css(".z--mb-16 .tec--badge::text").getall()

    categories_selector = selector.css(".tec--badge--primary::text").getall()

    return {
        "url": url_selector,
        "title": title_selector,
        "timestamp": timestamp_selector,
        "writer": writer_selector,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary_selector,
        "sources": [source.strip() for source in sources_selector],
        "categories": [category.strip() for category in categories_selector],
    }


# Requisito 5
def get_tech_news(amount):
    # https://app.betrybe.com/course/computer-science/redes-e-raspagem-de
    # -dados/raspagem-de-dados/ab38ab4e-bdbd-4984-8987-1abf32d85f26/conteudos/b63ffce8-be02-4be1-9b88-bda695400647/
    # recursos-paginados/96623da6-152d-49aa-8fec-6a34556a79df?use_case=side_bar

    # https://github.com/tryber/sd-010-b-tech-news/blob/3786d9a1c2d3517fb62267119321fe530a6fab25/tech_news/scraper.py
    # https://github.com/tryber/sd-010-b-tech-news/pull/12/files

    base_url = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(base_url)
    list_news_updates = scrape_novidades(html_content)

    database = []

    while len(list_news_updates) < amount:
        base_url = scrape_next_page_link(html_content)
        fetch_url = fetch(base_url)
        list_news_updates.extend(scrape_novidades(fetch_url))

    for new_url in list_news_updates[0:amount]:
        data = fetch(new_url)
        notice_html_content = scrape_noticia(data)
        database.append(notice_html_content)

    create_news(database)
    return database
