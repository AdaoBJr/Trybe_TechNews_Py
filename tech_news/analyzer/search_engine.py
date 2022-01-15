import tech_news.database as db


# Requisito 6
def search_by_title(title):
    news = db.find_news()
    news_list = []
    for new in news:
        if new["title"].lower() == title.lower():
            news_list.append((new["title"], new["url"]))
    return news_list


# Requisito 7
def search_by_date(date):
    pass


# Requisito 8
def search_by_source(source):
    news = db.find_news()
    sources_list = []
    for new in news:
        for ne in new["sources"]:
            if ne.lower() == source.lower():
                sources_list.append((new["title"], new["url"]))
    return sources_list


# Requisito 9
def search_by_category(category):
    news = db.find_news()
    category_list = []
    for new in news:
        for ne in new["categories"]:
            if ne.lower() == category.lower():
                category_list.append((new["title"], new["url"]))
    return category_list
