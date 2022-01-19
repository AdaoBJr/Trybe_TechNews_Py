from tech_news.database import search_news
import datetime


# FONTE lower(): https://shortest.link/2z5G
# Requisito 6
def search_by_title(title):
    searche_news = search_news({'title': {
        '$regex': title, '$options': 'index'}})
    news_by_title = []
    for new in searche_news:
        if new['title'].lower() == title.lower():
            item = new['title'], new['url']
            news_by_title.append(item)
    return news_by_title


# FONTE strptime(): encr.pw/Pf9PS
# Requisito 7
def date_format_validation(date_input):
    try:
        datetime.datetime.strptime(date_input, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def search_by_date(date):
    valid_date = date_format_validation(date)
    searched_news = search_news({'timestamp': {
        '$regex': date, '$options': 'index'}})
    news_by_date = []
    if valid_date:
        for new in searched_news:
            item = new['title'], new['url']
            news_by_date.append(item)
        return news_by_date
    else:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    searched_news = search_news({'sources': {
        '$regex': source, '$options': 'index'}})
    news_by_source = []
    for new in searched_news:
        item = new['title'], new['url']
        news_by_source.append(item)
    return news_by_source


# Requisito 9
def search_by_category(category):
    searched_news = search_news({'categories': {
        '$regex': category, '$options': 'index'}})
    news_by_category = []
    for new in searched_news:
        item = new['title'], new['url']
        news_by_category.append(item)
    return news_by_category
