import requests
import time
import re
from parsel import Selector
from tech_news.database import create_news
from tech_news.assistants import seletores, list_strip, URL_MAIN


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    if response.status_code == 200:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    html = Selector(html_content)
    return html.css(seletores["list_titles"]).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    html = Selector(html_content)
    return html.css(seletores["next_page"]).get()


# Requisito 4
def scrape_noticia(html_content):
    page = Selector(html_content)
    share_count = page.css(seletores["shares_count"]).get() or "0"
    comment_cout = page.css(seletores["comments_count"]).get() or "0"
    return {
        "url": page.css(seletores["url"]).get(),
        "title": page.css(seletores["title"]).get(),
        "timestamp": page.css(seletores["timestamp"]).get(),
        "writer": page.css(".z--font-bold").css("*::text").get().strip() or "",
        "shares_count": int(re.sub("[^0-9]", "", share_count)),
        "comments_count": int(comment_cout),
        "summary": "".join(page.css(seletores["sumary"]).getall()),
        "sources": list_strip(page.css(seletores["sources"]).getall()),
        "categories": list_strip(page.css(seletores["categories"]).getall()),
    }


# Requisito 5
def get_tech_news(amount, results=[], url=URL_MAIN):
    html_page = fetch(url)
    news = scrape_novidades(html_page)
    for new in news[: abs(amount - len(results))]:
        dict_new = scrape_noticia(fetch(new))
        results.append(dict_new)
    if len(results) >= amount:
        create_news(results)
        return results
    else:
        next_page = scrape_next_page_link(html_page)
        return get_tech_news(amount, results, next_page)
