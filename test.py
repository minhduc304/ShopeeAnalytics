import re
import requests

"""
Test file for new features or debugging
"""

url = 'https://shopee.vn/api/v4/shop/search_items?filter_sold_out=2&limit=10&offset=0&order=desc&shop_categoryids=110300684&shopid=109545884&sort_by=sales&use_case=2'
x = 'https://shopee.vn/api/v4/shop/get_categories?limit=20&offset=0&shopid=109545884'

request_ = requests.get(x)

content = request_.json()

id_list = []

# for category_id in content['data']['shop_categories']:
#     id = [x for x in category_id.values()]

#     id_list.append(id[0])

# print(id_list)

# for id in id_list:
#     url = 'https://shopee.vn/api/v4/shop/search_items?filter_sold_out=2&limit=10&offset=0&order=desc&shop_categoryids={}&shopid=109545884&sort_by=sales&use_case=2'.format(id)
#     content = requests.get(url)
#     print(content.text)


"""
Two api links
First url = https://{origin}/api/v4/shop/get_shop_detail?username={shop_name}  
***General shop info


Second url = https://shopee.vn/api/v4/shop/search_items?filter_sold_out=2&limit=10&offset=0&order=desc&shop_categoryids={category_id}&shopid={shop_id}&use_case=2
***List of all items, given a category id, a shop may have multiple category ids, each of which may have multiple items. 

"""



url_ = 'https://shopee.vn/api/v4/shop/get_shop_detail?sort_sold_out=0&username=atous.clothing'

request_ = requests.get(url_)
content = request_.json()

