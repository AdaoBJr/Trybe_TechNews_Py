import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        res = requests.get(url, timeout=3)
    except requests.exceptions.RequestException:
        return res.status_code
    else:
        if res.status_code == 200:
            return res
        return None
print(fetch('https://httpbin.org/delay/5'))