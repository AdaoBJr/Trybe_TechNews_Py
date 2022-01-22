import sys


# Requisito 12
def analyzer_menu():
    option_selected = input("""Selecione uma das opções a seguir:
        0 - Popular o banco com notícias;
        1 - Buscar notícias por título;
        2 - Buscar notícias por data;
        3 - Buscar notícias por fonte;
        4 - Buscar notícias por categoria;
        5 - Listar top 5 notícias;
        6 - Listar top 5 categorias;
        7 - Sair.""")

    answers = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a fonte:",
        "4": "Digite a categoria:",
        "5": "",
        "6": "",
        "7": "",
    }

    if option_selected not in answers:
        sys.stderr.write("Opção inválida")
    else:
        answer = answers[option_selected]
        new_option = input(answer)
        print(new_option)
