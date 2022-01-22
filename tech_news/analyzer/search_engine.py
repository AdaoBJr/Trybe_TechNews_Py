from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    matched_news = search_news({"title": {"$regex": title, "$options": "i"}})
    news_tuples = [(new["title"], new["url"]) for new in matched_news]
    return news_tuples


# Requisito 7

def validate_date(raw_date):
    try:
        datetime.strptime(raw_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def search_by_date(date):
    if validate_date(date):
        matched_news = search_news({
            "timestamp": {"$regex": date, "$options": "i"}})
        news_tuples = [(new["title"], new["url"]) for new in matched_news]
        return news_tuples
    else:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    matched_news = search_news({
        "sources": {"$regex": source, "$options": "i"}})
    news_tuples = [(new["title"], new["url"]) for new in matched_news]
    return news_tuples


# Requisito 9
def search_by_category(category):
    matched_news = search_news({
        "categories": {"$regex": category, "$options": "i"}})
    news_tuples = [(new["title"], new["url"]) for new in matched_news]
    return news_tuples
