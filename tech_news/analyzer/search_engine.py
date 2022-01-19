from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    news_list = []

    for report in news:
        if report["title"].lower() == title.lower():
            news_list.append((report["title"], report["url"]))

    return news_list


# Requisito 7
def search_by_date(date):
    news = search_news({"timestamp": {"$regex": date}})
    news_list = []
    try:
        datetime.strptime(date, "%Y-%m-%d")  # Documentação do Python
        for report in news:
            news_list.append((report["title"], report["url"]))
        return news_list

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = search_news(
        {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}}
    )
    news_list = []

    for report in news:
        news_list.append((report["title"], report["url"]))
    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
