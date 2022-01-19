from tech_news.database import search_news
from datetime import datetime

# Requisito 6


def search_by_title(title):
    result = [
        (news["title"], news["url"])
        for news in search_news(
            {"title": {"$regex": f"{title}", "$options": "i"}}
        )
    ]
    # The $options with ‘I’ parameter means case insensitivity
    return result


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    result = [
        (news["title"], news["url"])
        for news in search_news(
            {"timestamp": {"$regex": f"{date}", "$options": "i"}}
        )
    ]

    return result


# Requisito 8
def search_by_source(source):
    result = [
        (news["title"], news["url"])
        for news in search_news(
            {"sources": {"$regex": f"{source}", "$options": "i"}}
        )
    ]

    return result


# Requisito 9
def search_by_category(category):
    result = [
        (news["title"], news["url"])
        for news in search_news(
            {"categories": {"$regex": f"{category}", "$options": "i"}}
        )
    ]

    return result
