from tech_news.database import search_news


# Requisito 6
# recebi a ajuda do Bugs
# https://www.thecodebuzz.com/mongodb-query-case-sensitive-case-insensitive/
def search_by_title(title):
    news_found = search_news({"title": {'$regex': title, '$options': 'i'}})

    if len(news_found) != 0:
        for i in news_found:
            news_list = (
                i["title"],
                i["url"],
            )
            return [news_list]
    else:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
