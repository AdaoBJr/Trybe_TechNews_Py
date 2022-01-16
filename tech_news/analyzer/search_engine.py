import datetime
from tech_news.database import find_news


def getTitleAndUrl(fullNews):
    filteredNews = []

    for news in fullNews:
        filteredNews.append((news['title'], news['url']))

    return filteredNews


# Requisito 6
def search_by_title(title):
    allNews = find_news()

    fullNews = [n for n in allNews if title.lower() == n['title'].lower()]

    return getTitleAndUrl(fullNews)


# https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def validate(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_date(date):
    validate(date)

    allNews = find_news()

    fullNews = [n for n in allNews if date == n['timestamp'][0:10]]

    return getTitleAndUrl(fullNews)


# Requisito 8
def search_by_source(source):
    allNews = find_news()
    titleAndUrlNews = []

    for fullN in allNews:
        news = [fullN for n in fullN['sources'] if source.lower() == n.lower()]
        titleAndUrlNews.extend(getTitleAndUrl(news))

    return titleAndUrlNews


# Requisito 9
def search_by_category(category):
    allNews = find_news()
    titleAndUrlNews = []
    cat = category

    for fullN in allNews:
        news = [fullN for n in fullN['categories'] if cat.lower() == n.lower()]
        titleAndUrlNews.extend(getTitleAndUrl(news))

    return titleAndUrlNews
