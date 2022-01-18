from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = find_news()
    list_news = []

    for new in news:
        if new['title'].lower() == title.lower():
            list_news.append((new['title'], new['url']))

    return list_news

    # print(result[0])


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
