import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_source
from tech_news.analyzer.search_engine import search_by_category


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    options = input(
        "Selecione uma das opções a seguir:\n "
        "0 - Popular o banco com notícias;\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por fonte;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair.\n "
    )
    options_menu_p1(int(options))
    options_menu_p2(int(options))


def options_menu_p1(option):
    if option == 0:
        amount = input("Digite quantas notícias serão buscadas:")
        return get_tech_news(int(amount))
    if option == 1:
        title = input("Digite o título:")
        return print(search_by_title(title))
    if option == 2:
        date = input("Digite a data no formato aaaa-mm-dd:")
        return print(search_by_date(date))
    if option == 3:
        source = input("Digite a fonte:")
        return print(search_by_source(source))


def options_menu_p2(option):
    if option == 4:
        category = input("Digite a categoria:")
        return print(search_by_category(category))
    if option == 5:
        return print("Top 5 Noticias:")
    if option == 6:
        return print("Top 5 Categorias:")
    if option == 7:
        print("Encerrando script")
    if option >= 8:
        print("Opção inválida", file=sys.stderr)
