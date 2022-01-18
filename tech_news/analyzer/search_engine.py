# Requisito 6
import datetime
from tech_news.database import search_news


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    search_result = search_news(query)
    return (
        [(news["title"], news["url"]) for news in search_result]
        if len(search_result) > 0
        else []
    )


# Requisito 7
# https://www.codevscolor.com/date-valid-check-python
def search_by_date(date):
    year, month, day = [int(date_element) for date_element in date.split("-")]
    isValidDate = True
    try:
        datetime.date(year, month, day)
    except ValueError:
        isValidDate = False

    if isValidDate is False:
        raise ValueError("Data inválida")

    query = {"timestamp": {"$regex": date}}
    search_result = search_news(query)
    return (
        [(news["title"], news["url"]) for news in search_result]
        if len(search_result) > 0
        else []
    )


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": source, "$options": "i"}}
    search_result = search_news(query)
    return (
        [(news["title"], news["url"]) for news in search_result]
        if len(search_result) > 0
        else []
    )


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


""" a = search_by_date("2020-11-23")
print(a) """
