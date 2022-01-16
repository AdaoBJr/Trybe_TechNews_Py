from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    notice_list = find_news()
    title_url_list = []
    # print(notice_list, title)

    for notice in notice_list:
        if notice["title"] == title or notice["title"].upper() == title:
            title_url_list.append((notice["title"], notice["url"]))

    return title_url_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    # date = datetime.date.fromisoformat(date)
    notice_list = find_news()
    # print(notice_list, date)
    title_url_list = []

    for notice in notice_list:
        try:
            datetime.date.fromisoformat(date)
            if notice["timestamp"].find(date) == 0:
                title_url_list.append((notice["title"], notice["url"]))
        except ValueError:
            raise ValueError("Data inválida")

    return title_url_list


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    notice_list = find_news()
    print(notice_list, source)



# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
