from tech_news.database import db

# Requisito 6


def search_by_title(title):
    filtered_list = []
    news_list = db.news.find({"title": {"$regex": title, "$options": "i"}})
    for news in news_list:
        filtered_list.append((news["title"], news["url"]))
    return filtered_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
