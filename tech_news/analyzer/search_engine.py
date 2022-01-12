from tech_news.database import search_news
import datetime


def search(query):
    news_list = []
    search_list = search_news(query)
    for news in search_list:
        news_list.append((news["title"], news["url"]))

    return news_list


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    return search(query)


# Requisito 7
def search_by_date(date):
    separate_date = date.split("-")
    year = int(separate_date[0])
    month = int(separate_date[1])
    day = int(separate_date[2])
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        raise ValueError("Data inválida")

    date_query = f"^{date}"
    query = {"timestamp": {"$regex": date_query}}
    return search(query)


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": source, "$options": "i"}}
    return search(query)


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": category, "$options": "i"}}
    return search(query)
