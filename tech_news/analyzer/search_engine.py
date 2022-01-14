from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    data = find_news()
    result_list = []

    for el in data:
        if el["title"] == title:
            new_tuple = (el["title"], el["url"])
            result_list.append(new_tuple)

    return result_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
