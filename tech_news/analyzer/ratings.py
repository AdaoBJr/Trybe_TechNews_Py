from tech_news.database import find_news


# Requisito 10
def top_5_news():
    # https://docs.python.org/3/howto/sorting.html
    news = find_news()
    for new in news:
        new["popularity"] = new["shares_count"] + new["comments_count"]
    sorted_news = sorted(news, key=lambda new: new["popularity"], reverse=True)
    return [(new["title"], new["url"]) for new in sorted_news[:5]]


# Requisito 11
def top_5_categories():
    news = find_news()
    aux_categories_list = []
    for new in news:
        aux_categories_list += new['categories']
        print(aux_categories_list)
    aux_categories_list.sort()
    return aux_categories_list[:5]
