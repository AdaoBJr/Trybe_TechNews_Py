from parsel import Selector
import requests
import time
from tech_news.database import (
    create_news,
    # find_news,
)


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    else:
        if response.status_code == 200:
            return response.text
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    titles = selector.css("h3.tec--card__title a::attr(href)").getall()
    return titles


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".tec--list .tec--btn::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    news = {}
    selector = Selector(text=html_content)
    news["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    news["title"] = selector.css(".tec--article__header__title::text").get()
    news["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()
    news["writer"] = (
        "".join(
            selector.css(
                ".z--m-none.z--truncate.z--font-bold *::text"
            ).getall()
        ).strip()
        or "".join(
            selector.css(".tec--timestamp__item.z--font-bold *::text").getall()
        ).strip()
    )
    # r"\w+.+\w"
    news["shares_count"] = int(
        selector.css(".tec--toolbar__item::text").re_first(r"\d+") or 0
    )
    news["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get() or 0
    )
    news["summary"] = "".join(
        selector.css(".tec--article__body > p:first-of-type *::text").getall()
    )  # 1
    news["sources"] = selector.css(".z--mb-16 div a::text").re(r"\w+.+\w")
    categories = selector.css("#js-categories a::text").getall()
    news["categories"] = [category.strip() for category in categories]
    return news
    # news = {}
    # selector = Selector(text=html_content)
    # news["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    # news["title"] = selector.css(".tec--article__header__title::text").get()
    # news["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()
    # news["writer"] = (
    #     "".join(
    #         selector.css(
    #             ".z--m-none.z--truncate.z--font-bold *::text"
    #         ).getall()
    #     ).strip()
    #     or "".join(
    #         selector.css(".tec--timestamp__item.z--font-bold *::text").getall()
    #     ).strip()
    # )
    # # r"\w+.+\w"
    # news["shares_count"] = int(
    #     selector.css(".tec--toolbar__item::text").re_first(r"\d+") or 0
    # )
    # news["comments_count"] = int(
    #     selector.css("#js-comments-btn::attr(data-count)").get() or 0
    # )
    # # news["summary"] = "".join(
    # summary = selector.css("div.tec--article__body > p:first-child *::text").getall()
    # news["summary"] = "".join(summary)
    # print(
    #     "".join(
    #         selector.css(
    #             ".tec--article__body p:first-of-type *::text"
    #         ).getall()
    #     )
    # )
    # print(news["url"])

    # news["sources"] = selector.css(".z--mb-16 div a::text").re(r"\w+.+\w")
    # categories = selector.css("#js-categories a::text").getall()
    # cat = []
    # for category in categories:
    #     # print(category.strip())
    #     cat.append(category.strip())
    # print(cat)
    # news["categories"] = cat
    # # news["categories"] = selector.css("#js-categories a::text").re(r"\w+.+\w")
    # return news


# Requisito 5
def get_tech_news(amount):
    # url = "https://www.tecmundo.com.br/novidades"
    # res = fetch(url)
    # link_list = scrape_novidades(res)
    # scrapy_results = []
    # while len(link_list) < amount:
    #     url = scrape_next_page_link(res)
    #     res = fetch(url)
    #     # aqui também poderia ser usado o extend para adicionar no
    #     # final da lista
    #     link_list += scrape_novidades(res)
    # # Tricks para array em python
    # # https://gist.github.com/RatulSaha/b41c52614da34762a74d16dc066b68df
    # for notice_link in link_list[0:amount]:
    #     html = fetch(notice_link)
    #     scrapy_of_page = scrape_noticia(html)
    #     scrapy_results.append(scrapy_of_page)
    # create_news(scrapy_results)
    # return scrapy_results
    next_page = "https://www.tecmundo.com.br/novidades"
    url_news_list = scrape_novidades(fetch(next_page))
    news_list = []
    while len(url_news_list) < amount:
        next_page = scrape_next_page_link(fetch(next_page))
        url_news_list.extend(scrape_novidades(fetch(next_page)))
    url_news_list = url_news_list[:amount]
    for news in url_news_list:
        news_list.append(scrape_noticia(fetch(news)))
    create_news(news_list)
    # return find_news()
    return news_list


# news = get_tech_news(3)
# print(news)
# for new in news:
#     print(new)


"""
# 1:
https://stackoverflow.com/questions/58904013/extract-text-content-from-nested-html-while-excluding-some-specific-tags-scrapy
"""
