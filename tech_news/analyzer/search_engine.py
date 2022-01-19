from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    news_database = find_news()
    new_list = []

    for new in news_database:
        if new["title"].lower() == title.lower():
            new_list.append((new["title"], new["url"]))
    return new_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
