from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    list_news = find_news()
    # return list_news
    for a in list_news:
        # calcular a sua "popularidade" 
        # somando seu número de compartilhamentos e comentários.
        sum = a["shares_count"] + a["comments_count"]
        a["popularity"] = sum
        # print(a)
    # A função deve ordenar as notícias por ordem de popularidade.
    # Em caso de empate, o desempate deve ser por ordem alfabética de título.
    list_news = sorted(list_news, key=lambda x: x["title"])
    list_news = sorted(list_news, key=lambda x: x["popularity"], reverse=True)
    
    return_five = list_news[:5]
    return return_five


def sort_list(list):
    sorted = list.sort()
    top_5_categories = sorted[:5]
    return top_5_categories


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    top_categories = []
    list_news = find_news()
    if (list_news):
        for index in list_news:
            top_categories.extend(index["categories"])
        numbers_of_categories = list(Counter(top_categories).keys())
        res = sort_list(numbers_of_categories)
        return res
    else:
        return []
