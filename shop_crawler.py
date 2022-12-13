from datetime import datetime
import csv
import pandas as pd
from shopee_crawler import Crawler
import os
import json
from tqdm import tqdm
import concurrent.futures
from util.reset_proxies import reset_proxies



def shop_crawler(url, folder_save='crawl_data_follow_shopID'):
    """
    comment
    """

    crawler = Crawler()

    crawler.set_origin(origin="shopee.vn")

    items_in_shop = {}
    content, total_count, length = crawler.crawl_by_shop_url(url)

    # splits the shop json by product and assign keys to them
    for index, item in enumerate(content):
        items_in_shop[index] = item


    shop_id = 0

    #finds the current shop's id
    for product in content:
        shop_id = product['shop_id']

        if shop_id != 0:
            break

    now = datetime.now()
    fetched_time = now.strftime("%Y_%m_%d_%H_%M")

    #data for log file
    data = [shop_id, total_count if total_count == length else length, fetched_time]


    #create folder shopID
    path_shopID = os.path.join(folder_save, str(shop_id))

    isExist = os.path.exists(path_shopID)
    if not isExist:
        os.makedirs(path_shopID)
        
    #naming the file containing the json content collected of a shop specific to the time
    name_file_data_crawled = '$'.join([str(shop_id), str(total_count), str(fetched_time)]) + '.json'


    path_with_day = os.path.join(path_shopID, name_file_data_crawled)
    #if the json file of a shop at a specific time doesn't already exist
    #add the products dictionary to newly created json file
    if not os.path.exists(path_with_day):
        with open(path_with_day, 'a+') as f:
            json.dump(items_in_shop, f)

    with open('log.csv', 'a+') as f:
        writer = csv.writer(f)
        #writer.writerow(fields)
        writer.writerow(data)    


with open('datascr/urls_mall.txt', 'r') as f:
    urls_mall = f.readlines()



def main(if_reset_proxies, max_workers):
    #update to new proxies for every new query
    if if_reset_proxies: 
        reset_proxies()

    #optimizing the crawler by performing threading
    #for every 
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
        results = list(tqdm(executor.map(shop_crawler, urls_mall), total = len(urls_mall)))
    return results


if __name__ == '__main__':
    main(if_reset_proxies=False, max_workers=32)

# for url in tqdm(urls_mall):
#     shop_crawler(url) 
