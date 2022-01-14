import re


def get_url(selector):
    url = selector.css("link[rel=canonical]::attr(href)").get()
    return url


def get_title(selector):
    title = selector.css("h1.tec--article__header__title::text").get()
    return title


def get_timestamp(selector):
    timestamp = selector.css("time::attr(datetime)").get()
    return timestamp


def get_writer(selector):
    writer = selector.css(
        "#js-author-bar >"
        "div > p.z--m-none.z--truncate.z--font-bold >"
        "a::text"
    ).get()

    if writer is None:
        writer = selector.css(
            "#js-main > div > article > div.tec--article__body-grid > " +
            "div.z--pt-40.z--pb-24 > div.z--flex.z--items-center > "
            "div.tec--timestamp.tec--timestamp--lg > " +
            "div.tec--timestamp__item.z--font-bold > a::text"
        ).get()

    if writer is None:
        writer = selector.css(
            "#js-author-bar > div > p.z--m-none.z--truncate.z--font-bold::text"
        ).get()

    if writer is not None:
        writer = writer.strip()

    return writer


def get_shares_count(selector):
    shares_count = selector.css("div.tec--toolbar__item::text")

    if len(shares_count) == 0:
        shares_count = 0
    else:
        shares_count = re.findall(r"\d+", shares_count.get())[0]

    return int(shares_count)


def get_comments_count(selector):
    comments_count = selector.css("button.tec--btn::attr(data-count)").get()

    if comments_count is not None:
        return int(comments_count)

    return 0


def get_summary(selector):
    summary = selector.css(
        "div.tec--article__body " "p:nth-child(1) *::text"
    ).getall()
    return "".join(summary)


def get_sources(selector):
    sources = selector.css("div.z--mb-16 > div > a.tec--badge::text").getall()

    return [source.strip() for source in sources]


def get_categories(selector):
    categories = selector.css("div#js-categories > a::text").getall()

    return [category.strip() for category in categories]
