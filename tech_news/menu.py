# Requisito 12

def analyzer_menu():
    # https://www.ti-enxame.com/pt/python/criando-um-menu-em-python/1043095475/

    options = input("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.""")

    resolution = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
    }

    try:
        print(resolution[options])
    except KeyError:
        print("Opção inválida\n")
