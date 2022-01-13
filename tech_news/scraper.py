import requests
import time
from parsel import Selector
import tech_news.database as db_connection


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(response.encoding)
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url_list = selector.css(".tec--card__info a::attr(href)").getall()
    if len(url_list):
        return url_list
    return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url_list = selector.css(".tec--btn::attr(href)").get()
    if url_list:
        return url_list
    return None


def scrape_url(selector):
    url = selector.css("head > link[rel='canonical']::attr(href)").get()
    return url


def scrape_title(selector):
    title = selector.css('h1::text').get()
    if title:
        return title
    return ''


def scrape_timeStamp(selector):
    timeStamp = selector.css('time::attr(datetime)').get()
    if timeStamp:
        return timeStamp
    return ''


def scrape_writer(selector):
    writer = selector.css('.tec--author__info a::text').get()
    if writer:
        return writer
    return None


def scrape_shares(selector):
    shares = selector.css('.tec--toolbar__item::text').get()
    if shares:
        if 'Compartilharam' in shares:
            return int(shares[:-len(' Compartilharam')])
    return 0


def scrape_comments(selector):
    comments = selector.css('#js-comments-btn::attr(data-count)').get()
    return int(comments)


def scrape_summary(selector):
    path = '.tec--article__body p:nth-child(1) *::text'
    summary = selector.css(path).getall()
    return ''.join(summary)


def scrape_sources(selector):
    sources = selector.css('.z--mb-16 .tec--badge::text').getall()
    return sources


def scrape_categories(selector):
    categories = selector.css('#js-categories a::text').getall()
    return categories


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news = {
        'url': scrape_url(selector),
        'title': scrape_title(selector),
        'timeStamp': scrape_timeStamp(selector),
        'writer': scrape_writer(selector),
        'shares_count': scrape_shares(selector),
        'comments_count': scrape_comments(selector),
        'summary': scrape_summary(selector),
        "sources": scrape_sources(selector),
        "categories": scrape_categories(selector)
    }
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    search_results = []
    html = fetch('https://www.tecmundo.com.br/novidades')
    while len(search_results) <= amount:
        news_link = scrape_novidades(html)
        for news in news_link:
            if len(search_results) <= amount:
                search_results.append(scrape_noticia(news))
        next_link = scrape_next_page_link(html)
        html = fetch(next_link)
    db_connection.create_news(search_results)
    return search_results
