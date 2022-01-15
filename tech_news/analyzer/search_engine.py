import tech_news.database as db


# Requisito 6
def search_by_title(title):
    found_news = db.find_news()
    return [
        (notice["title"], notice["url"])
        for notice in found_news
        if title.lower() in notice["title"].lower()
    ]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
