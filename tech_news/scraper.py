import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.text
    except requests.HTTPError:
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    response = selector.css(
        ".tec--list--lg .tec--card__title > a ::attr(href)"
    ).getall()
    return response


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    response = selector.css("div.tec--list.tec--list--lg "
                            "> a ::attr(href)").get()
    return response


# Requisito 4

def get_url(selector):
    return selector.css("head > link[rel=canonical] ::attr(href)").get()
    
    
def get_title(selector):
    return selector.css("#js-article-title ::text").get()
    
    
def get_timestamp(selector):
    return selector.css("#js-article-date ::attr(datetime)").get()
    
    
def get_writer(selector):
    query = [
        ".tec--author__info__link::text",
        ".tec--timestamp a::text",
        "#js-author-bar > div p::text",
    ]
    for item in query:
        writer = selector.css(item).get()
        if writer is not None:
            return writer.strip()
    return None
      
    
def get_shares_count(selector):
    shares_count = selector.css("#js-author-bar > nav > "
                                "div:nth-child(1) ::text").get()
    if shares_count is not None:
        return shares_count.strip().split(" ")[0]
    return 0 


def get_comments_count(selector):
    return selector.css("#js-comments-btn ::attr(data-count)").get()
    # comments = selector.css("#js-comments-btn ::attr(data-count)").getall()
    # if commnets is not []:
    #     list_comments = list(map(lambda x: x.strip(), comments))
    #     list_filter = list(filter(lambda x: x != "", comments))
    #     return list_filter
    # return None


def get_summary(selector):
    summary = "".join(selector.css(".p402_premium > "
                                   "p:nth-child(1) ::text").getall())
    if summary is not None:
        return summary
    
    return None


def get_sources(selector):
    sources = selector.css(".z--mb-16 > div > a::text").getall()
    if sources is not []:        
        list_categories = list(map(lambda x: (x.strip()), sources))
        return list(filter(lambda x: x != "", list_categories))
    return None


def get_categories(selector):
    # Ajuda do Pedro Henrique 
    categories = selector.css("#js-categories ::text").getall()
    list_categories = list(map(lambda x: (x.strip()), categories))
    return list(filter(lambda x: x != "", list_categories))


def scrape_noticia(html_content):
    selector = Selector(html_content)
    info = {}
    info["url"] = get_url(selector)
    info["title"] = get_title(selector)
    info["timestamp"] = get_timestamp(selector)
    info["writer"] = get_writer(selector)
    info["shares_count"] = int(get_shares_count(selector))
    info["comments_count"] = int(get_comments_count(selector))
    info["summary"] = get_summary(selector)
    info["sources"] = get_sources(selector)
    info["categories"] = get_categories(selector)
    return info


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
