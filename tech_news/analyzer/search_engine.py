from tech_news.database import db
import re
import datetime


# Requisito 6
def search_by_title(title):
    # consulta no =https://stackoverflow
    # .com/questions/6266555/querying-mongodb-via-pymongo-in-case-insensitive-efficiently
    get_title = db.news.find({"title": re.compile(title, re.IGNORECASE)})
    return [(item["title"], item["url"]) for item in get_title]


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        get_date = db.news.find({"timestamp": re.compile(date, re.IGNORECASE)})
    except ValueError:
        raise ValueError("Data inválida")
    return [(item["title"], item["url"]) for item in get_date]


# Requisito 8
def search_by_source(source):
    get_source = db.news.find(
        {"sources": re.compile(source, re.IGNORECASE)})
    return [(item["title"], item["url"]) for item in get_source]


# Requisito 9
def search_by_category(category):
    get_category = db.news.find(
        {"categories": re.compile(category, re.IGNORECASE)}
    )
    return [(item["title"], item["url"]) for item in get_category]


if __name__ == "__main__":
    print(search_by_title("Vamoscomtudo"))
