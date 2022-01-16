from datetime import datetime


def format_news(array_news):
    result = []
    for news in array_news:
        result.append((news['title'], news['url']))
    return result


def is_valid_date(data):
    try:
        datetime.strptime(data, '%Y-%m-%d')
        return True
    except ValueError:
        raise ValueError("Data inválida")
