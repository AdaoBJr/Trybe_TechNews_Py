from ..database import search_news
import re


# Requisito 6
def search_by_title(title):
    results = []
    for result in search_news({"title": {"$regex": title, "$options": "i"}}):
        results.append((result["title"], result["url"]))
    return results


def compare_month_days(month, day):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if int(day) > (days[int(month) - 1]):
        return True
    return False


# Requisito 7
def search_by_date(date):
    MATCH = r"^\d{4}-\d{2}-\d{2}$"
    date_data = date.split("-")
    if not bool(
        re.match(MATCH, date)) or int(
            date_data[1]) > 12 or int(
                date_data[2]) > 31 or compare_month_days(
                    date_data[1], date_data[2]):
        raise ValueError("Data inválida")
    results = []
    for result in search_news({"timestamp": {"$regex": date}}):
        results.append((result["title"], result["url"]))
    return results


# Requisito 8
def search_by_source(source):
    results = []
    for result in search_news(
            {"sources": {"$regex": source, "$options": "i"}}):
        results.append((result["title"], result["url"]))
    return results


# Requisito 9
def search_by_category(category):
    results = []
    for result in search_news(
            {"categories": {"$regex": category, "$options": "i"}}):
        results.append((result["title"], result["url"]))
    return results
