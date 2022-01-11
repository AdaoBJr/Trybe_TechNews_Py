from parsel import Selector
import requests
import time


response = requests.get('https://www.tecmundo.com.br/novidades').text
selector = Selector(text=response)
links = selector.css('.tec--card__title a::attr(href)').getall()
print(links)