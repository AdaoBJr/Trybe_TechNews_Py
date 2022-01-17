from tech_news.database import find_news

# Requisito 6


def search_by_title(title):
    filtered_list = []
    news_list = find_news()
    for news in news_list:
        if title.lower() in news["title"].lower():
            filtered_list.append((news["title"], news["url"]))
    return filtered_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    filtered_list = []
    result = find_news()
    for news in result:
        for i in range(len(news["sources"])):
            news["sources"][i] = news["sources"][i].lower()
        if source.lower() in news["sources"]:
            filtered_list.append((news["title"], news["url"]))
    return filtered_list


# Requisito 9 -
def search_by_category(category):
    filtered_list = []
    result = find_news()
    for news in result:
        for i in range(len(news["categories"])):
            news["categories"][i] = news["categories"][i].lower()
        if category.lower() in news["categories"]:
            filtered_list.append((news["title"], news["url"]))
    return filtered_list
