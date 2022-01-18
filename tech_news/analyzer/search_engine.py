from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    founded_news = search_news({"title": {"$regex": title, "$options": "i"}})
    news_title_tuple = []
    for news in founded_news:
        news_title_tuple.append((news["title"], news["url"]))
    return news_title_tuple


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        founded_news = search_news({
            "timestamp": {
                "$regex": date,
                "$options": "i"
                }
            })
        news_datetime_tuple = []
        for news in founded_news:
            news_datetime_tuple.append((news["title"], news["url"]))
        return news_datetime_tuple
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    source_news = {
        "sources": {"$regex": source, "$options": "i"}
            }
    founded_news = search_news(source_news)
    news_title_tuple = []
    for news in founded_news:
        news_title_tuple.append((news["title"], news["url"]))
    return news_title_tuple


# Requisito 9
# The function must receive the full category name as a parameter.
# The function should fetch the news from the database by category.
# The function must return in the same format as the previous requirement.
# If no news is found, an empty list must be returned.
# The search must be case insensitive
def search_by_category(category):
    category_news = {
        "categories": {"$regex": category, "$options": "i"}
            }
    founded_news = search_news(category_news)
    news_title_tuple = []
    for news in founded_news:
        news_title_tuple.append((news["title"], news["url"]))
    return news_title_tuple
