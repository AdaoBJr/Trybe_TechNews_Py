import datetime
from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    news_database = find_news()
    new_list = []

    for new in news_database:
        if new["title"].lower() == title.lower():
            new_list.append((new["title"], new["url"]))
    return new_list


# Requisito 7
def search_by_date(date):
    news_database = find_news()
    new_list = []

    try:
        datetime.datetime.fromisoformat(date)
        for new in news_database:
            if new["timestamp"][0:10] == date:
                new_list.append((new["title"], new["url"]))

        return new_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news_database = find_news()
    new_list = []

    for new in news_database:
        for source_data in new["sources"]:
            if source_data.lower() == source.lower():
                new_list.append((new["title"], new["url"]))

    return new_list


# Requisito 9
def search_by_category(category):
    news_database = find_news()
    new_list = []

    for new in news_database:
        for category_data in new["categories"]:
            if category_data.lower() == category.lower():
                new_list.append((new["title"], new["url"]))

    return new_list
