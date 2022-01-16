from tech_news.database import search_news
import datetime


def valid_date(date):
    try:
        return datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 6
def search_by_title(title):
    response = search_news({"title": {"$regex": title, "$options": "i"}})

    ZERO = 0
    if len(response) > ZERO:
        for result in response:
            lists = [(result["title"], result["url"])]
            return lists
    return []


# Requisito 7
def search_by_date(date):
    response = search_news({"timestamp": {"$regex": date}})
    date_validation = valid_date(date)

    if date_validation:
        for result in response:
            lists = [(result["title"], result["url"])]
            return lists
    return []


# Requisito 8
def search_by_source(source):
    response = search_news(
        {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}}
    )

    ZERO = 0
    if len(response) > ZERO:
        for result in response:
            lists = [(result["title"], result["url"])]
            return lists
    return []


# Requisito 9
def search_by_category(category):
    response = search_news(
        {"categories": {"$elemMatch": {"$regex": category, "$options": "i"}}}
    )

    ZERO = 0
    if len(response) > ZERO:
        for result in response:
            lists = [(result["title"], result["url"])]
            return lists

    return []
