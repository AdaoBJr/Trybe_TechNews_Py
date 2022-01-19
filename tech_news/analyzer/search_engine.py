from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    news_found = find_news()
    news_list = []
    for news in news_found:
        if news["title"].lower() == title.lower():
            news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
