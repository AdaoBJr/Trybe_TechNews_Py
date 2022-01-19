from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    data_news = find_news()
    list_result = []

    for element in data_news:
        if element["title"].lower() == title.lower():
            list_result.append((element["title"], element["url"]))
    return list_result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    data_news = find_news()
    list_result = []
    try:
        datetime.datetime.fromisoformat(date)
        for element in data_news:
            if element["timestamp"][0:10] == date:
                list_result.append((element["title"], element["url"]))
        return list_result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    data_news = find_news()
    list_result = []

    for element in data_news:
        for index in element["sources"]:
            if index.lower() == source.lower():
                list_result.append((element["title"], element["url"]))
    return list_result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    data_news = find_news()
    list_result = []

    for element in data_news:
        for index in element["categories"]:
            if index.lower() == category.lower():
                list_result.append((element["title"], element["url"]))
    return list_result
