from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm

# reset proxies list 
def reset_proxies():
    options_ = Options()
    options_.headless = True
    url_ = 'https://free-proxy-list.net/'

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options_)
    driver.get(url_)

    proxies = driver.find_elements('xpath', '//td[1]')
    
    print("Updating list with new proxies.")

    with open('proxies.txt', 'w') as f:
        # limited to 300 because the column containing the proxy ips contained other unnecessary data
        for proxy in tqdm(proxies[:300]):
            f.write(proxy.text + '\n')
    
    print("Proxies list has been updated.")

