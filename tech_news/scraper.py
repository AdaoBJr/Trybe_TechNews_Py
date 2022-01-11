import requests
from parsel import Selector
from time import sleep


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

    url = html_content
    title = select.css("#js-article-title ::text").get()
    timestamp = select.css("#js-article-date ::attr(datetime)").get()
    writer = (
        select.css("p.z--m-none.z--truncate.z--font-bold a::text")
        .get()
        .strip()
    )
    shares_count = select.css("svg.feather.z--mr-8 use::text").get()

    return shares_count
    # comments_count - número de comentários que a notícia recebeu. Ex: 26
    # summary - o primeiro parágrafo da notícia. Ex:"O CEO da Tesla, Elon Musk, garantiu que a montadora está muito perto de atingir o chamado nível 5 de autonomia de sistemas de piloto automático de carros. A informação foi confirmada em uma mensagem enviada pelo executivo aos participantes da Conferência Anual de Inteligência Artificial (WAIC, na sigla em inglês). O evento aconteceu em Xangai, na China, onde a montadora comemora resultados positivos de mercado."
    # sources - lista contendo fontes da notícia. Ex: ["Venture Beat", "Source 2"]
    # categories - lista de categorias que classificam a notícia. Ex: ["Mobilidade Urbana/Smart Cities", "Veículos autônomos", "Tesla", "Elon Musk"]


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
