from ..database import find_news


# Requisito 6
# def low_str(s):
#     return s.upper()


# def mod_values(d, mod):
#     d.upadte(title=mod(d["title"]))
#     return d


# def low_values_list(normal_list):
#     print(normal_list, 'lsit')
#     new_list = []
#     for item in normal_list:
#         low_item = mod_values(item, low_str)
#         new_list.append(upp_item)
#     return new_list


def search_by_title(title):
    # find_news()
    # news_update = low_values_list(find_news())

    # print(news_update, 'news')
    # for notice in news_update:
    #     insert_or_update(notice)
    # result = []
    # news_full = search_news({"title": low_str(title)})

    # if len(news_full) < 1:
    #     return []
    # else:
    #     for new in news_full:
    #         result.append((new["title"], new["url"]))
    #     return result
    data = find_news()
    result = []
    for notice in data:
        if notice["title"].lower() == title.lower():
            result.append((notice["title"], notice["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
