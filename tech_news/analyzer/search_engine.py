from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    dbNews = find_news()
    data = []
    for news in dbNews:
        if news["title"].lower() == title.lower():
            data.append((news["title"], news["url"]))
    return data


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
