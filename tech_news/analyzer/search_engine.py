from tech_news.database import search_news
import re
# from tech_news.scraper import get_tech_news
# import time


# Requisito 6
def search_by_title(title):
    result_list = []
    query = {"title": re.compile(title, re.IGNORECASE)}
    search_result = search_news(query)

    for el in search_result:
        result_list.append((el["title"], el["url"]))

    return result_list


# Requisito 7
def search_by_date(date):
    pass


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# get_tech_news(3)
# title = "VAMOSCOMTUDO"
# print(search_by_title(title))

# Requisito 7
# # get_tech_news(10)
# timestamp = "2022-01-14"
# print(search_by_date(timestamp))
