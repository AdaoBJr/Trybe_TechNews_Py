# Requisito 1
def fetch(url):
     time.sleep(1)
    try:
      res = requesting.get(url, timeout=3)
      res.raise_for_status()
    except requesting.HTTPError:
      return None
    except requesting.Timeout:
      return None
    return res.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
