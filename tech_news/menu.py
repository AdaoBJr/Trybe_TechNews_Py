import sys


# Requisito 12
def print_options(options):
    for option in options:
        print(option, end=" ")


def analyzer_menu():
    options = [
        "Selecione uma das opções a seguir:\n",
        "0 - Popular o banco com notícias;\n",
        "1 - Buscar notícias por título;\n",
        "2 - Buscar notícias por data;\n",
        "3 - Buscar notícias por fonte;\n",
        "4 - Buscar notícias por categoria;\n",
        "5 - Listar top 5 notícias;\n",
        "6 - Listar top 5 categorias;\n",
        "7 - Sair."
    ]

    print_options(options)
    option_selected = input()

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
