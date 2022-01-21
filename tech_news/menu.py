import sys


# Requisito 12
case = {
    # Caso a opção 0 seja selecionada, seve-se exibir a mensagem "Digite quantas notícias serão buscadas:"
    "0": "Digite quantas notícias serão buscadas:",
    # Caso a opção 1 seja selecionada, deve-se exibir a mensagem "Digite o título:";
    "1": "Digite o título:",
    # Caso a opção 2 seja selecionada, deve-se exibir a mensagem "Digite a data no formato aaaa-mm-dd:";
    "2": "Digite a data no formato aaaa-mm-dd:",
    # Caso a opção 3 seja selecionada, deve-se exibir a mensagem "Digite a fonte:";
    "3": "Digite a fonte:",
    # Caso a opção 4 seja selecionada, deve-se exibir a mensagem "Digite a categoria:";
    "4": "Digite a categoria:"
}


def analyzer_menu():
    """Seu código deve vir aqui"""
    """
    O texto exibido pelo menu deve ser exatamente:
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
    select_menu = input(
        "Selecione uma das opções a seguir:\n"
        "0 - Popular o banco de dados com notícias;\n"
        "1 - Buscar notícias por título;\n"
        "2 - Buscar notícias por data;\n"
        "3 - Buscar notícias por fonte;\n"
        "4 - Buscar notícias por categoria;\n"
        "5 - Listar top 5 notícias;\n"
        "6 - Listar top 5 categorias;\n"
        "7 - Sair."
    )
    if select_menu in case.keys():
        input_info = input(case[select_menu])
        return input_info
    else:
      # Caso a opção não exista, exiba a mensagem de erro
      # "Opção inválida" na stderr
      print("Opção inválida", file=sys.stderr)
