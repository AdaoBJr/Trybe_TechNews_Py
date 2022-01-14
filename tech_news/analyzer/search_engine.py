from tech_news.database import search_news

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


print(search_by_title("VAMOSCOMTUDO"))


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
