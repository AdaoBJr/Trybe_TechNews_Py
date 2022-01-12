from tech_news.analyzer.search_engine import search_by_title
from tech_news.database import find_news


def ordenacao_popularidade(news_dict):
    keys_list = []
    # ordenação decrescente de titulos pela popularidade
    # realizado com pesquisa em
    # https://diegomariano.com/como-ordenar-um-dicionario-em-python/
    for title in sorted(news_dict, key=news_dict.get, reverse=True):
        keys_list.append(title)
    return keys_list


# Requisito 10
def top_5_news():
    news_dict = {}
    news_list = []
    all_news = find_news()
    # Cria um dicionário onde a chave é titulo e o valor a popularidade
    for news in all_news:
        soma = 0
        soma += news["shares_count"] + news["comments_count"]
        news_dict[news["title"]] = soma

    title_list = ordenacao_popularidade(news_dict)
    for title in title_list[:5]:
        news_list.extend(search_by_title(title))

    return news_list


# Requisito 11
def top_5_categories():
    categories_list = []
    all_news = find_news()
    for news in all_news:
        categories_list.extend(news["categories"])

    # Ordena em ordem alfabética
    categories_list = sorted(categories_list)

    # Cria um dict onde a chave é o index e o valor a quantidade de ocorrencias
    categories_dict = {}
    for i in range(len(categories_list)):
        category = categories_list[i]
        categories_dict[i] = categories_list.count(category)

    # Ordena de forma decrecente
    index_list = ordenacao_popularidade(categories_dict)

    top_5_list_categories = []
    for index in index_list[:5]:
        top_5_list_categories.append(categories_list[index])

    return top_5_list_categories
