from tech_news.database import search_news
import datetime

# Requisito 6
# recebi a ajuda do Bugs
# https://www.thecodebuzz.com/mongodb-query-case-sensitive-case-insensitive/
def search_by_title(title):
    news_found = search_news({"title": {'$regex': title, '$options': 'i'}})

    if len(news_found) != 0:
        for i in news_found:
            news_list = (
                i["title"],
                i["url"],
            )
            return [news_list]
    else:
        return []


def valid_date(date, format):
    try:
        return datetime.datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
# recebi ajuda da Camila Arruda
def search_by_date(date):
    format = "%Y-%m-%d"
    valid = valid_date(date, format)

    news_found = search_news({"timestamp": {'$regex': date}})

    if valid:
        for i in news_found:
            news_list = (
                i["title"],
                i["url"],
            )
            return [news_list]
    return []


# Requisito 8
def search_by_source(source):
    news_found = search_news({"sources": {'$regex': source, '$options': 'i'}})

    if len(news_found) != 0:
        for i in news_found:
            news_list = (
                i["title"],
                i["url"],
            )
            return [news_list]
    else:
        return []


# Requisito 9
def search_by_category(category):
    news_found = search_news({"categories": {'$regex': category, '$options': 'i'}})

    if len(news_found) != 0:
        for i in news_found:
            news_list = (
                i["title"],
                i["url"],
            )
            return [news_list]
    else:
        return []
