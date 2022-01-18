import datetime
from tech_news.database import search_news


def execute_search(field_to_search, value, ignore_case=True):
    query = {field_to_search: {"$regex": value, "$options": "i"}}

    if ignore_case is False:
        query = {field_to_search: {"$regex": value}}
    search_result = search_news(query)

    return (
        [(news["title"], news["url"]) for news in search_result]
        if len(search_result) > 0
        else []
    )


# Requisito 6
def search_by_title(title):
    return execute_search("title", title)


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

    return execute_search("timestamp", date, ignore_case=False)


# Requisito 8
def search_by_source(source):
    return execute_search("sources", source)


# Requisito 9
def search_by_category(category):
    return execute_search("categories", category)
