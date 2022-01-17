import datetime
from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    news_finder = find_news()
    news_list = []

    for item in news_finder:
        if item['title'].upper() == title.upper():
            model = (item['title'], item['url'])
            news_list.append(model)
    return news_list


# Requisito 7
def search_by_date(date):
    news_finder = find_news()
    news_list = []
    try:
        datetime.date.fromisoformat(date)
        #  https://docs.python.org/3/library/datetime.html
        for item in news_finder:
            if item['timestamp'][:10] == date:
                news_list.append((item['title'], item['url']))
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    pass
    # news_finder = find_news()
    # news_list = []

    # for item in news_finder:
    #     formated_list = map(lambda x: x.lower(), item['sources'])
    #     # https://www.delftstack.com/pt/howto/python/python-lowercase-list/
    #     formated_source = source.lower()
    #     if formated_source in formated_list:
    #         news_list.append((item['title'], item['url']))
    # return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


if __name__ == '__main__':
    pass
    # print(search_by_title('ok'))
    # print(search_by_date('2020-11-23'))
    print(search_by_source('ResetEra'))
    # print(search_by_category())
