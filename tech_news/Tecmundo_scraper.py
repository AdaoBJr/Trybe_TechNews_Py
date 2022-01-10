class Scrap_tecmundo:
    def __init__(self, selector) -> None:
        self.selector = selector
        self.url = self.__find_url()
        self.title = self.__find_title()
        self.timestamp = self.__find_timestamp()
        self.writer = self.__find_writer()
        self.shares_count = self.__find_shares_count()
        self.comments_count = self.__find_comments_count()
        self.summary = self.__find_summary()
        self.sources = self.__find_sources()
        self.categories = self.__find_categories()

    def __find_url(self):
        return self.selector.css(
            "head > link[rel=canonical]::attr(href)"
        ).get()

    def __find_title(self):
        return self.selector.css(".tec--article__header__title::text").get()

    def __find_timestamp(self):
        return self.selector.css("time::attr(datetime)").get()

    def __find_writer(self):
        query_selectors = [
            ".tec--author__info__link::text",
            ".tec--timestamp a::text",
            "#js-author-bar > div p::text",
        ]
        for query in query_selectors:
            result = self.selector.css(query).get()
            if result is not None:
                return result.strip()
        return None

    def __find_shares_count(self):
        shares_count = 0
        try:
            shares_count = int(
                self.selector.css(".tec--toolbar__item::text").re(r"\d+")[0]
            )
        except IndexError:
            return 0
        finally:
            if shares_count is not None:
                return shares_count
            return 0

    def __find_comments_count(self):
        comments_count = 0
        try:
            comments_count = int(
                self.selector.css("#js-comments-btn::text").re(r"\d+")[0]
            )
        except IndexError:
            return 0
        finally:
            if comments_count is not None:
                return comments_count
            return 0

    def __find_summary(self):
        # symbol '>' doest work, only empty space
        return "".join(
            self.selector.css(
                ".tec--article__body > p:nth-child(1) *::text"
            ).getall()
        )

    def __find_sources(self):
        return [
            source.strip()
            for source in self.selector.css(
                ".z--mb-16 > div > a::text"
            ).getall()
            if source not in [" ", "Fontes"]
        ]

    def __find_categories(self):
        return [
            category.strip()
            for category in self.selector.css(
                "#js-categories *::text"
            ).getall()
            if category != " "
        ]

    def mount(self):
        return {
            "url": self.url,
            "title": self.title,
            "timestamp": self.timestamp,
            "writer": self.writer,
            "shares_count": self.shares_count,
            "comments_count": self.comments_count,
            "summary": self.summary,
            "sources": self.sources,
            "categories": self.categories,
        }
