
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
    pass


def get_comments_count(selector):
    pass


def get_summary(selector):
    pass


def get_sources(selector):
    pass


def get_categories(selector):
    pass
