import re


# Auxiliar Requisito 4
def get_news_url(selector):
    url_link = selector.css('link[rel=canonical] ::attr(href)').get()
    return url_link


# Auxiliar Requisito 4
def get_news_title(selector):
    news_title = selector.css('h1.tec--article__header__title ::text').get()
    return news_title


# Auxiliar Requisito 4
def get_news_timestamp(selector):
    news_timestamp = selector.css(
        'div.tec--timestamp__item time ::attr(datetime)').get()
    return news_timestamp


# Auxiliar Requisito 4
def get_news_writer(selector):
    news_writer = selector.css('a.tec--author__info__link ::text').get()
    if news_writer is None:
        news_writer = selector.css(
            'div.tec--timestamp div:nth-child(2) a ::text').get()
        if news_writer is None:
            news_writer = selector.css('p.z--m-none ::text').get()
    return news_writer


# FONTE Regular Expressions: https://shortest.link/2Epe
# FONTE Regular Expressions: https://www.youtube.com/watch?v=K8L6KVGG-7o
# Auxiliar Requisito 4
def get_news_shares_count(selector):
    shares_number = selector.css(
        'div.tec--toolbar__item::text').get()
    if shares_number:
        shares_number = int(re.findall(r'\d+', shares_number)[0])
    else:
        shares_number = 0
    return shares_number


# Auxiliar Requisito 4
def get_news_comments_count(selector):
    news_comments = selector.css(
        'button#js-comments-btn ::attr(data-count)').get()
    return int(news_comments)


# Auxiliar Requisito 4
def get_news_summary(selector):
    select_news_summary = selector.css(
        'div.tec--article__body p:nth-child(1) *::text').getall()
    return ''.join(select_news_summary)


# Auxiliar Requisito 4
def get_news_sources(selector):
    news_sources = selector.css('div.z--mb-16 div a ::text').getall()
    return [source.strip() for source in news_sources]


# Auxiliar Requisito 4
def get_news_categories(selector):
    news_categories = selector.css('div#js-categories a ::text').getall()
    return [category.strip() for category in news_categories]

