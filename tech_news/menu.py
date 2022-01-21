import sys


# Requisito 12
def analyzer_menu():
    menu = input("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.""")

    calls = {
        "0": lambda: int(input("Digite quantas notícias serão buscadas:")),
        "1": lambda: input("Digite o título:"),
        "2": lambda: input("Digite a data no formato aaaa-mm-dd:"),
        "3": lambda: input("Digite a fonte:"),
        "4": lambda: input("Digite a categoria:"),
    }

    try:
        calls[menu]()
    except KeyError:
        sys.stderr.write("Opção inválida\n")
