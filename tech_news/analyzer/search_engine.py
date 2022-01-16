from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    founded_news = search_news({"title": {"$regex": title, "$options": "i"}})
    news_title_tuple = []
    for news in founded_news:
        news_title_tuple.append((news["title"], news["url"]))
    return news_title_tuple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
