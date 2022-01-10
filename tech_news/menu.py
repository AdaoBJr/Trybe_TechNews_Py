import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


options = (
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

specific_options = {
    0: "Digite quantas notícias serão buscadas:\n",
    1: "Digite o título:\n",
    2: "Digite a data no formato aaaa-mm-dd:\n",
    3: "Digite a fonte:\n",
    4: "Digite a categoria:\n",
}

# lambda with no args
execute = {
    0: lambda: get_tech_news(int(input(specific_options[0]))),
    1: lambda: search_by_title(str(input(specific_options[1]))),
    2: lambda: search_by_date(str(input(specific_options[2]))),
    3: lambda: search_by_source(str(input(specific_options[3]))),
    4: lambda: search_by_category(str(input(specific_options[4]))),
    5: lambda: top_5_news(),
    6: lambda: top_5_categories(),
    7: lambda: print("Encerrando script"),
}


def analyzer_menu():
    try:
        option = int(input(options))
        print(execute[option]())
    except (KeyError, ValueError):
        sys.stderr.write("Opção inválida\n")
