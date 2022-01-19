import sys


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
    response = int(input("Digite quantas notícias serão buscadas: "))


def get_news_by_title():
    response = str(input("Digite o título: "))


def get_news_by_date():
    response = str(input("Digite a data no formato aaaa-mm-dd: "))


def get_news_by_source():
    response = str(input("Digite a fonte: "))


def get_news_by_category():
    response = str(input("Digite a categoria: "))


def get_top_five_popular_news():
    print('buscando top 5 noticias populares')


def get_top_five_popular_categories():
    print('buscando top 5 categoria populares')


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
