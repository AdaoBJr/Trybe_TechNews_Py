from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_source
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_news
from tech_news.analyzer.ratings import top_5_categories
import sys


# Requisito 12
def analyzer_menu():
    options = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )
    action = {
        "0": lambda: get_tech_news(
            int(input("Digite quantas notícias serão buscadas:"))
        ),
        "1": lambda: search_by_title(input("Digite o título:")),
        "2": lambda: search_by_date(
            input("Digite a data no formato aaaa-mm-dd:")
        ),
        "3": lambda: search_by_source(input("Digite a fonte:")),
        "4": lambda: search_by_category(input("Digite a categoria:")),
        "5": lambda: top_5_news(),
        "6": lambda: top_5_categories(),
        "7": lambda: print("Encerrando script"),
    }

    try:
        print(action[options]())
    except KeyError:
        sys.stderr.write("Opção inválida\n")
