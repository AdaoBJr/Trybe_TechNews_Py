from datetime import datetime
import re
from tech_news.database import (
    search_news,
)


# 3
def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime(
            "%Y-%m-%d"
        ):
            raise ValueError
        return True
    except ValueError:
        return False


# Requisito 6
def search_by_title(title):
    regx = re.compile(".*(%s).*" % title, re.IGNORECASE)  # 1, 2
    data = search_news({"title": regx})
    return [(news["title"], news["url"]) for news in data]


# Requisito 7
def search_by_date(date):
    if not validate(date):
        raise ValueError("Data inválida")
    regx = re.compile("^(%s)" % date, re.IGNORECASE)  # 1, 2
    data = search_news({"timestamp": regx})
    return [(news["title"], news["url"]) for news in data]


# Requisito 8
def search_by_source(source):
    regx = re.compile("(%s)" % source, re.IGNORECASE)  # 1, 2
    data = search_news({"sources": regx})
    return [(news["title"], news["url"]) for news in data]


# Requisito 9
def search_by_category(category):
    regx = re.compile("(%s)" % category, re.IGNORECASE)  # 1, 2
    data = search_news({"categories": regx})
    return [(news["title"], news["url"]) for news in data]


"""
# 1:
https://stackoverflow.com/questions/24637917/how-to-add-a-variable-into-my-re-compile-expression
# 2:
https://stackoverflow.com/questions/3483318/performing-regex-queries-with-pymongo
# 3:
https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python

"""
