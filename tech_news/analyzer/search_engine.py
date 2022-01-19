from tech_news.database import find_news
import datetime


# Agradecimento aos amigos:
# Felippe Correa,
# João Herculano
# Rafael Mathias e
# Lucas Lotar
# pela companhia e auxílio

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
    news_found = find_news()
    news_list = []
    try:
        datetime.datetime.fromisoformat(date)
        for news in news_found:
            if news["timestamp"][0:10] == date:
                news_list.append((news["title"], news["url"]))
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news_found = find_news()
    news_list = []
    for news in news_found:
        for index in news["sources"]:
            if index.lower() == source.lower():
                news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 9
def search_by_category(category):
    news_found = find_news()
    news_list = []
    for news in news_found:
        for index in news["categories"]:
            if index.lower() == category.lower():
                news_list.append((news["title"], news["url"]))
    return news_list
