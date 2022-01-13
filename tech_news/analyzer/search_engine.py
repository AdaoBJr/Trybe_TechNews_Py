from tech_news.database import find_news
import datetime
# Requisito 6


def search_by_title(title):
    all_news = find_news()
    result = []
    for news in all_news:
        if news['title'].lower() == title.lower():
            result.append((news['title'], news['url']))
    return result


# Requisito 7
# https://pythonhelp.wordpress.com/2011/11/12/fatiamento-slicing-de-strings-em-python/#:~:text=print%20s%5B%2D1%5D%20!,da%20string%20que%20queremos%20acessar.
# https://qastack.com.br/programming/16870663/how-do-i-validate-a-date-string-format-in-python
def search_by_date(date):
    all_news = find_news()
    result = []
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        for news in all_news:
            if news["timestamp"][0:10] == date:
                result.append((news["title"], news["url"]))
        print(result)
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
