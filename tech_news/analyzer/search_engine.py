from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_list = find_news()
    result = []
    for news in news_list:
        if (news['title'].lower() == title.lower()):
            result.append((news['title'], news['url']))

    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
