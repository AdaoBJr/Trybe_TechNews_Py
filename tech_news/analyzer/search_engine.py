import datetime
from ..database import find_news


# Requisito 6
def search_by_title(title):
    data = find_news()
    result = []
    for notice in data:
        if notice["title"].lower() == title.lower():
            result.append((notice["title"], notice["url"]))
    return result


# Requisito 7
def search_by_date(date):
    data = find_news()
    result = []

    try:
        datetime.date.fromisoformat(date)
        for notice in data:
            if notice["timestamp"].split("T")[0] == date:
                result.append((notice["title"], notice["url"]))
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
# https://stackoverflow.com/questions/1801668/convert-a-list-with-strings-all-to-lowercase-or-uppercase
def search_by_source(source):
    data = find_news()
    result = []
    for notice in data:
        for i in range(len(notice["sources"])):
            notice["sources"][i] = notice["sources"][i].lower()
            if notice["sources"][i] == source.lower():
                result.append((notice["title"], notice["url"]))
    return result


# Requisito 9
def search_by_category(category):
    data = find_news()
    result = []
    for notice in data:
        for i in range(len(notice["categories"])):
            notice["categories"][i] = notice["categories"][i].lower()
            if notice["categories"][i] == category.lower():
                result.append((notice["title"], notice["url"]))
    return result
