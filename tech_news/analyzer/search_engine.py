from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    response = find_news()
    search = []
    for new in response:
        if new["title"].lower() == title.lower():
            search.append((new["title"], new["url"]))
    return search


# Requisito 7
def search_by_date(date):
    response = find_news()
    search = []
    try:
        # https://docs.python.org/3/library/datetime.html
        datetime.date.fromisoformat(date)
        for new in response:
            if new["timestamp"][0:10] == date:
                search.append((new["title"], new["url"]))
        return search
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    response = find_news()
    search = []
    for new in response:
        # https://blog.betrybe.com/python/python-range/
        for i in range(len(new["sources"])):
            new["sources"][i] = new["sources"][i].lower()
        if source.lower() in new["sources"]:
            search.append((new["title"], new["url"]))
    return search


# Requisito 9
def search_by_category(category):
    response = find_news()
    search = []
    for new in response:
        for i in range(len(new["categories"])):
            new["categories"][i] = new["categories"][i].lower()
        if category.lower() in new["categories"]:
            search.append((new["title"], new["url"]))
    return search
