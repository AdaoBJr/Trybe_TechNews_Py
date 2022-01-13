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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


if __name__ == '__main__':
    print(search_by_title('ok'))
    # print(search_by_date())
    # print(search_by_source())
    # print(search_by_category())
