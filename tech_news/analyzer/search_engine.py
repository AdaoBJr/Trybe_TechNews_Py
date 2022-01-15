import tech_news.database as db_connection


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, '$options': 'i'}}
    news = db_connection.search_news(query)
    filtered_news = []
    if len(news):
        for data in news:
            filtered_news.append((data['title'], data['url']))
        return filtered_news
    return news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
