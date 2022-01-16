from tech_news.database import search_news
from tech_news.utils.utils import return_tuple_list, validate_date
import re

# from tech_news.scraper import get_tech_news


# Requisito 6
def search_by_title(title):
    query = {"title": re.compile(title, re.IGNORECASE)}
    search_result = search_news(query)

    return return_tuple_list(search_result)


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
    query = {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}}
    search_result = search_news(query)

    return return_tuple_list(search_result)


# Requisito 9
def search_by_category(category):
    query = {
        "categories": {"$elemMatch": {"$regex": category, "$options": "i"}}
    }

    search_result = search_news(query)

    return return_tuple_list(search_result)


# source = "ResetEra"
# print(search_by_source(source))
