from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager




options_ = Options()
options_.headless = True
url_ = 'https://shopee.vn/mall/brands'

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options_)
driver.get(url_)

all_data = driver.find_elements('xpath', "//div[contains(@class, 'official-shop-brand-list__section-wrapper')]")
urls = driver.find_elements('xpath', './/a[@href]')

with open('urls.txt', 'w') as f:
    for url in urls:
        f.write(url.get_attribute('href') + '\n')
#     print(url.get_attribute('href'))


