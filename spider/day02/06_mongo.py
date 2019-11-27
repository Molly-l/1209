import pymongo

#1.连接对象
conn=pymongo.MongoClient('localhost',27017)
# 2.库对象
db=conn['syudb']
# 3.集合对象
myset=db['stuset']

myset.insert_one({'name':'小明'})
print()