from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    teste = find_news()
    list_result = []

    for element in teste:
        if element["title"].lower() == title.lower():
            list_result.append((element["title"], element["url"]))
    return list_result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
