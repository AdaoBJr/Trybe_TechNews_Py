from tech_news.analyzer.search_engine import search_by_title
from tech_news.database import find_news


def ordenacao_popularidade(news_dict):
    title_list = []
    # ordenação decrescente de titulos pela popularidade
    # realizado com pesquisa em 
    # https://diegomariano.com/como-ordenar-um-dicionario-em-python/
    for title in sorted(news_dict, key=news_dict.get, reverse=True):
        title_list.append(title)
    return title_list


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
    """Seu código deve vir aqui"""
