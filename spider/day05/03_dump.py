import json

item_list = [ {'name':'大圣娶亲'},{'name':'月光宝盒'} ]

with open('douban.json','a') as f:
    json.dump(item_list,f,ensure_ascii=False)


















