from tech_news.database import find_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    res = find_news()
    tupleList = []
    for news in res:
        if news["title"].lower() == title.lower():
            tupleList.append((news["title"], news["url"]))
    return tupleList


# Requisito 7
def search_by_date(date):
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime
    res = find_news()
    tupleList = []
    try:
        parsedDate = datetime.strptime(date, "%Y-%m-%d")
        for news in res:
            currentDate = news["timestamp"][0:10]
            currentDate = datetime.strptime(currentDate, "%Y-%m-%d")
            if parsedDate.date() == currentDate.date():
                tupleList.append((news["title"], news["url"]))

    except Exception:
        raise ValueError("Data inválida")
    return tupleList


# Requisito 8
def search_by_source(source):
    res = find_news()
    tupleList = []
    source = source.lower()
    for news in res:
        sources = news["sources"]
        sources = list(map(lambda x: x.lower(), sources))

        if source in sources:
            tupleList.append((news["title"], news["url"]))

    return tupleList


# Requisito 9
def search_by_category(category):
    res = find_news()
    tupleList = []
    category = category.lower()
    for news in res:
        categories = news["categories"]
        categories = list(map(lambda x: x.lower(), categories))

        if category in categories:
            tupleList.append((news["title"], news["url"]))

    return tupleList
