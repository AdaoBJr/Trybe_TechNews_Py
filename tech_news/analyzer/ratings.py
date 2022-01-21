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
    # A função deve ter retorno no mesmo formato do requisito anterior,
    # porém limitado a 5 notícias.
    five = [list_news for list_news in list_news[:5]]
    my_arr = []
    for a in list_news:
        my_arr.append(tuple([a["title"], a["url"]]))
    return my_arr


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    top_categories = []
    list_news = find_news()
    if (list_news):
        for index in list_news:
            top_categories.extend(index["categories"])
        numbers_of_categories = list(Counter(top_categories).keys())
        numbers_of_categories.sort()
        top_5_categories = numbers_of_categories[:5]
        return top_5_categories
    else:
        return []
