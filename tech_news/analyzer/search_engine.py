from tech_news.database import find_news
import datetime

# Requisito 6
def search_by_title(title):
    data_news = find_news()
    list_result = []

    for element in data_news:
        if element["title"].lower() == title.lower():
            list_result.append((element["title"], element["url"]))
    return list_result


# Requisito 7
def search_by_date(date):
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


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
