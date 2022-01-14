from tech_news.database import search_news
from datetime import datetime

# https://www.w3schools.com/python/python_mongodb_query.asp
# https://www.kite.com/python/answers/how-to-find-the-values-of-a-key-in-a-list-of-dictionaries-in-python#:~:
# text=Use%20a%20list%20comprehension%20to,the%20list%20of%20dictionaries%20list_of_dicts%20.
# https://www.thecodebuzz.com/mongodb-query-case-sensitive-case-insensitive/


# Requisito 6
def search_by_title(title):
    news_found = search_news({"title": {'$regex': title, '$options': 'i'}})

    zero = 0
    if len(news_found) is not zero:
        for tuple in news_found:
            title_and_url = (
                tuple["title"],
                tuple["url"],
            )
            return [title_and_url]
    else:
        return []
    """Seu código deve vir aqui"""


# https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
# https://www.geeksforgeeks.org/python-validate-string-date-format/

def check_date_format(date):
    format = "%Y-%m-%d"
    try:
        return bool(datetime.strptime(date, format))
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_date(date):
    valid_format = check_date_format(date)
    news_found = search_news({"timestamp": {'$regex': date}})
    zero = 0
    print(len(news_found))

    if valid_format:
        for tuple in news_found:
            title_and_url = (
                tuple["title"],
                tuple["url"],
            )
            return [title_and_url]
    if len(news_found) is zero:
        return []
    else:
        return valid_format


# Requisito 8
def search_by_source(source):
    news_found = search_news({"sources": {'$regex': source, '$options': 'i'}})

    zero = 0
    if len(news_found) is not zero:
        for tuple in news_found:
            title_and_url = (
                tuple["title"],
                tuple["url"],
            )
            return [title_and_url]
    else:
        return []


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
