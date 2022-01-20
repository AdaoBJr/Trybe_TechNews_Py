import sys
from tech_news.analyzer.search_engine import search_by_title, search_by_date
from tech_news.analyzer.search_engine import search_by_source
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.scraper import get_tech_news

title = """
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
 """


def populate_database():
    amount = int(input("Digite quantas notícias serão buscadas: "))
    response = get_tech_news(amount)
    print(response)


def get_news_by_title():
    title = str(input("Digite o título: "))
    response = search_by_title(title)
    print(response)


def get_news_by_date():
    date = str(input("Digite a data no formato aaaa-mm-dd: "))
    response = search_by_date(date)
    print(response)


def get_news_by_source():
    source = str(input("Digite a fonte: "))
    response = search_by_source(source)
    print(response)


def get_news_by_category():
    category = str(input("Digite a categoria: "))
    response = search_by_category(category)
    print(response)


def get_top_five_popular_news():
    response = top_5_news()
    print(response)


def get_top_five_popular_categories():
    response = top_5_categories()
    print(response)


menu = {
    0: populate_database,
    1: get_news_by_title,
    2: get_news_by_date,
    3: get_news_by_source,
    4: get_news_by_category,
    5: get_top_five_popular_news,
    6: get_top_five_popular_categories,
}


# Requisito 12
def analyzer_menu():
    try:
        response = int(input(title))
    except ValueError:
        return ValueError('Opção inválida')

    if(response == 7):
        print('Encerrando script\n')
    elif(0 <= response <= 6):
        menu[response]()
    else:
        sys.stderr.write("Opção inválida\n")
