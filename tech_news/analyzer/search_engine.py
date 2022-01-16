from tech_news.database import search_news
from tech_news.utils.utils import return_tuple_list, validate_date
import re
# from tech_news.scraper import get_tech_news


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
    is_date = validate_date(date)
    if not is_date:
        query = {"timestamp": {"$regex": date}}
        search_result = search_news(query)

        return return_tuple_list(search_result)
    else:
        raise ValueError("Data inválida")


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
# timestamp = "21-12-1980"
# timestamp = "2020-11-23"
# print(search_by_date(timestamp))
