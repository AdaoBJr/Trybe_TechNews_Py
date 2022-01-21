import sys


# Requisito 12
case = {
    # Caso a opção 0 seja selecionada,
    # deve-se exibir a mensagem "Digite quantas notícias serão buscadas:"
    "0": "Digite quantas notícias serão buscadas:",
    # Caso a opção 1 seja selecionada,
    # deve-se exibir a mensagem "Digite o título:";
    "1": "Digite o título:",
    # Caso a opção 2 seja selecionada,
    # deve-se exibir a mensagem "Digite a data no formato aaaa-mm-dd:";
    "2": "Digite a data no formato aaaa-mm-dd:",
    # Caso a opção 3 seja selecionada,
    # deve-se exibir a mensagem "Digite a fonte:";
    "3": "Digite a fonte:",
    # Caso a opção 4 seja selecionada,
    # deve-se exibir a mensagem "Digite a categoria:";
    "4": "Digite a categoria:"
}


def analyzer_menu():
    select_menu = input(
        "Selecione uma das opções a seguir:"
        "0 - Popular o banco com notícias;\n"
        "1 - Buscar notícias por título;\n"
        "2 - Buscar notícias por data;\n"
        "3 - Buscar notícias por fonte;\n"
        "4 - Buscar notícias por categoria;\n"
        "5 - Listar top 5 notícias;\n"
        "6 - Listar top 5 categorias;\n"
        "7 - Sair."
    )
    calls = {
        "0": lambda: int(input("Digite quantas notícias serão buscadas:")),
        "1": lambda: input("Digite o título:"),
        "2": lambda: input("Digite a data no formato aaaa-mm-dd:"),
        "3": lambda: input("Digite a fonte:"),
        "4": lambda: input("Digite a categoria:"),
    }
    try:
        calls[select_menu]()
    except KeyError:
        sys.stderr.write("Opção inválida\n")
