from datetime import datetime
import csv
import pandas as pd
from shopee_crawler import Crawler
import os
import json
from tqdm import tqdm


def shop_crawler(url, foler_save='crawl_data_follow_shopID'):
    crawler = Crawler()

    crawler.set_origin(origin="shopee.vn")

    items_in_shop = {}
    content, total_count, length = crawler.crawl_by_shop_url(url)

    for index, item in enumerate(content):
        items_in_shop[index] = item


    shop_id = 0

    for product in content:
        shop_id = product['shop_id']

        if shop_id != 0:
            break

    now = datetime.now()
    fetched_time = now.strftime("%Y_%m_%d_%H_%M")


    fields = ['shop_id', 'product_number', 'fetched_time']
    data = [shop_id, total_count if total_count == length else length, fetched_time]


    # create folder shopID
    path_shopID = os.path.join(foler_save, str(shop_id))

    isExist = os.path.exists(path_shopID)
    if not isExist:
        os.makedirs(path_shopID)
        


    name_file_data_crawled = '$'.join([str(shop_id), str(total_count), str(fetched_time)]) + '.json'

    path_with_day = os.path.join(path_shopID, name_file_data_crawled)
    if not os.path.exists(path_with_day):
        with open(path_with_day, 'a+') as f:
            json.dump(items_in_shop, f)

    with open('log.csv', 'a+') as f:
        writer = csv.writer(f)
        #writer.writerow(fields)
        writer.writerow(data)    

with open('urls_mall.txt', 'r') as f:
    urls_mall = f.readlines()
for url in tqdm(urls_mall):
    shop_crawler(url)