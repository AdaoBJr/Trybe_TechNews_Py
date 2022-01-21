from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    my_arr = []
    list_news = find_news()
    # return list_news


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
