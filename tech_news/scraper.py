from parsel import Selector
import time
import requests


selector_url="head > link[rel=canonical]::attr(href)"
selector_title="h1.tec--article__header__title::text"
selector_timestamp="div.tec--timestamp__item > time::attr(datetime)"
selector_writer="div.tec--author a.tec--author__info__link::text"
selector_shares_count=".tec--toolbar > .tec--toolbar__item::text"
selector_comments_count=".tec--toolbar > .tec--toolbar__item > button::attr(data-count)"
path_sumary="string(/html/body/div[1]/main/div[1]/article/div[3]/div[2]/p[1])"
path_sources="/html/body/div[1]/main/div[1]/article/div[3]/div[4]/div/a/text()"
path_categories="/html/body/div[1]/main/div[1]/article/div[3]/div[5]/div/a/text()"


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None

    if(response.status_code == 200):
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    notice = selector.css("div.tec--list")
    links = notice.css("figure a.tec--card__thumb__link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link = selector.css("div.tec--list > a.tec--btn::attr(href)").get()
    return link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css(selector_url).get()
    title = selector.css(selector_title).get()
    timestamp = selector.css(selector_timestamp).get()
    writer = selector.css(selector_writer).get()[1:]
    shares_count = selector.css(selector_shares_count).get()
    comments_count = selector.css(selector_comments_count).get()
    summary = selector.xpath(path_sumary).get()
    sources = selector.xpath(path_sources).getall()
    categories = selector.xpath(path_categories).getall()
    return{'url': url, 'title': title, 'timestamp': timestamp, 'writer': writer, 
    'shares_count': 'shares_count', 'comments_count': comments_count, 
    'summary': summary, 'sources': sources, 'categories': categories}


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


