import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        res = requests.get(url, timeout=3)
    except requests.exceptions.RequestException:
        return None
    else:
        if res.status_code == 200:
            return res.text
        return None
print(fetch('https://www.tecmundo.com.br/novidades'))