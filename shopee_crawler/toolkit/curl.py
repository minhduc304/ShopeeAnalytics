from tabnanny import check
import requests
import random
import time

random.seed(10)

def get_header():
    return {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'content-type': 'text'
    }

def retry_with_backoff(retries=3, backoff_in_seconds=1):
    def rwb(func):
        def wrapper(url):
            x = 0
            while True:
                try:
                    return func(url)
                except:
                    if x == retries:
                        raise
                    else:
                        sleep = (backoff_in_seconds * 2 ** x +
                                 random.uniform(0, 1))
                        time.sleep(sleep)
                        x += 1
        return wrapper
    return rwb


@retry_with_backoff()
def curl(url: str, timeout: int=3) -> dict:
    with open('checked_proxies.txt', 'r') as f:
        # list of proxies (potentially) blocked by the site 
        checked_proxies = f.readlines()

    with open('proxies.txt') as f:
        proxies = f.readlines()

    # filters out only the proxies that have been (potentially) blocked
    proxy_in_use = [x for x in proxies if x not in checked_proxies]
    while True:
        # changes proxy being used after every iteration
        proxy_idx = random.randint(0, len(proxy_in_use) - 1)
        try:
            response = requests.get(
                url,
                headers=get_header(),
                timeout=timeout).json() #, 
                #proxies={'http':'http://{}'.format(proxy_in_use[proxy_idx])}).json()
            print(response)
            
        except:
            with open('checked_proxies.txt', 'a+') as f:
                f.write(proxy_in_use[proxy_idx])
            
            print("Error, looking for another proxy")
        return response