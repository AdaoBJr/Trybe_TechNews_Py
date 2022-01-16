import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    css_selector = '.tec--list--lg h3.tec--card__title > a ::attr(href)'
    url_list = selector.css(css_selector).getall()
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
    css_selectors = [
        ".tec--author__info__link::text",
        ".tec--timestamp a::text",
        "#js-author-bar > div p::text",
    ]
    for query in css_selectors:
        writer = selector.css(query).get()
        if writer is not None:
            return writer.strip()
    return None


def scrape_shares(selector):
    shares = selector.css('.tec--toolbar__item::text').get()
    if shares:
        if 'Compartilharam' in shares:
            return int(shares[:-len(' Compartilharam')])
    return 0


def scrape_comments(selector):
    comments = selector.css('#js-comments-btn::attr(data-count)').get()
    if comments:
        return int(comments)
    return None


def scrape_summary(selector):
    path = '.tec--article__body > p:nth-child(1) *::text'
    summary = selector.css(path).getall()
    return ''.join(summary)


def scrape_sources(selector):
    sources = selector.css('.z--mb-16 .tec--badge::text').getall()
    trimmed_list = []
    for source in sources:
        trimmed_list.append(source.strip())
    return trimmed_list


def scrape_categories(selector):
    categories = selector.css('#js-categories a::text').getall()
    trimmed_list = []
    for category in categories:
        trimmed_list.append(category.strip())
    return trimmed_list


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news = {
        'url': scrape_url(selector),
        'title': scrape_title(selector),
        'timestamp': scrape_timeStamp(selector),
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
    html = fetch('https://www.tecmundo.com.br/novidades')
    news_urls = scrape_novidades(html)
    search_results = []
    while len(news_urls) < amount:
        url = scrape_next_page_link(html)
        html = fetch(url)
        news_urls.extend(scrape_novidades(html))
    for news in news_urls:
        if len(search_results) < amount:
            news_html = fetch(news)
            news_data = scrape_noticia(news_html)
            search_results.append(news_data)
    create_news(search_results)
    return search_results
