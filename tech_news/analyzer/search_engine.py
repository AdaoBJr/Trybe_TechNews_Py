import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    selected_news = search_news(query)
    tupla_title_url = [(item["title"], item["url"]) for item in selected_news]

    return tupla_title_url


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        query = {"timestamp": {"$regex": date, "$options": "i"}}
        selected_news = search_news(query)
        tupla_title_url = [
            (item["title"], item["url"]) for item in selected_news]

        return tupla_title_url

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": source, "$options": "i"}}
    selected_news = search_news(query)
    tupla_title_url = [(item["title"], item["url"]) for item in selected_news]

    return tupla_title_url


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": category, "$options": "i"}}
    selected_news = search_news(query)
    tupla_title_url = [(item["title"], item["url"]) for item in selected_news]

    return tupla_title_url
