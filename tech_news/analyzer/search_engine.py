# Requisito 6
from tech_news.database import find_news
import datetime


def search_by_title(title):
    content = find_news()
    result = [
        (new["title"], new["url"])
        for new in content
        if new["title"].lower() == title.lower()
    ]
    return result


# Requisito 7
def search_by_date(date):
    content = find_news()
    try:
        datetime.date.fromisoformat(date)   # Alessandra Rezende
        result = [
            (new["title"], new["url"])
            for new in content
            if new["timestamp"][0:10] == date
        ]
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    content = find_news()

    for new in content:
        for s in range(len(new["sources"])):
            new["sources"][s] = new["sources"][s].lower()

    result = [
        (new["title"], new["url"])
        for new in content
        if source.lower() in new["sources"]
    ]

    return result


# Requisito 9
def search_by_category(category):
    content = find_news()

    for new in content:
        for c in range(len(new["categories"])):
            new["categories"][c] = new["categories"][c].lower()

    result = [
        (new["title"], new["url"])
        for new in content
        if category.lower() in new["categories"]
    ]

    return result
