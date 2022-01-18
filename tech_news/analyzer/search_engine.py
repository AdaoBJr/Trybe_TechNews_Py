import re
from tech_news.database import (
    search_news,
)


# Requisito 6
def search_by_title(title):
    regx = re.compile(".*(%s).*" % title, re.IGNORECASE)  # 1, 2
    data = search_news({"title": regx})
    return [(news['title'], news['url']) for news in data]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


"""
# 1:
https://stackoverflow.com/questions/24637917/how-to-add-a-variable-into-my-re-compile-expression
# 2:
https://stackoverflow.com/questions/3483318/performing-regex-queries-with-pymongo
"""
