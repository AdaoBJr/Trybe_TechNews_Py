import re
# Source https://qastack.com.br/programming/4289331/how-to-extract-numbers-
# from-a-string-in-python
# URL LINK Jonathan Souza


def get_url(selector):
    return selector.css("link[rel=canonical]::attr(href)").get()


def get_title(selector):
    return selector.css("h1.tec--article__header__title::text").get()


def get_timestamps(selector):
    return selector.css(
        "div.tec--timestamp__item time::attr(datetime)").get()


def get_writer(selector):
    writer = selector.css("a.tec--author__info__link::text").get()
    if writer is None:
        writer = selector.css(
            "div.tec--timestamp div:nth-child(2) a::text").get()
        if writer is None:
            writer = selector.css("p.z--m-none::text").get()
    return writer


def get_shares_count(selector):
    shares_count = selector.css("div.tec--toolbar__item::text").get()
    if shares_count:
        shares_count = int(re.findall(r'\d+', shares_count)[0])
    else:
        shares_count = 0
    return shares_count


def get_comments_count(selector):
    return selector.css(
        "button#js-comments-btn::attr(data-count)").get()


def get_summary(selector):
    summary = selector.css(
        "div.tec--article__body p:nth-child(1) *::text").getall()
    return ''.join(summary)


def get_sources(selector):
    sources = selector.css("div.z--mb-16 div a::text").getall()
    return [i.strip() for i in sources]


def get_categories(selector):
    categories = selector.css("div#js-categories a::text").getall()
    return [i.strip() for i in categories]
