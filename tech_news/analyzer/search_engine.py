from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    search_news = find_news()
    news_by_title = []
    for new in search_news:
        if new['title'].lower() == title.lower():
            news_by_title.append((new['title'], new['url']))
    return news_by_title


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
