import requests
import time
import re
from parsel import Selector
from tech_news.database import create_news
from tech_news.assistants import seletores, list_strip


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
# AJUDA DA ALESSANDRA REZENDE
def get_tech_news(amount):
    base_url = "https://www.tecmundo.com.br/novidades"
    fetch_url = fetch(base_url)
    notice_list = scrape_novidades(fetch_url)
    notice_result = []

    while len(notice_list) < amount:
        base_url = scrape_next_page_link(fetch_url)
        fetch_url = fetch(base_url)
        notice_list.extend(scrape_novidades(fetch_url))

    for notice_url in notice_list[0:amount]:
        data = fetch(notice_url)
        notice = scrape_noticia(data)
        notice_result.append(notice)

    create_news(notice_result)
    return notice_result
