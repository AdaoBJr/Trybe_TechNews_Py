from ..database import find_news


# Requisito 10
def top_5_news():
    popularity_list = []
    for item in find_news():
        popularity = int(item["shares_count"])+int(item["comments_count"])
        popularity_list.append((item["title"], item["url"], popularity))
    # https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
    sorted_list = sorted(popularity_list, key=lambda tup: tup[2], reverse=True)
    top_five = sorted_list[0:5]
    result = []
    for news in top_five:
        result.append((news[0], news[1]))
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
