'''
pymongo的使用
'''

import pymongo

#连接数据库
conn = pymongo.MongoClient('127.0.0.1', 27017)

#生成数据库对象
db = conn.t1

#生成集合对象
myset = db.class1

#数据操作：增删改查，索引聚合
# ##############################插入操作#########################
# print(dir(myset))
# myset.insert_one({'name':'张铁林', 'King':'乾隆'})
# myset.insert_many([{'name':'张国立', 'King':'康熙'}, {'name':'陈建斌', 'King':'雍正'}])
# myset.save({'_id':1, 'name':'聂远', 'King':'乾隆'})

################################查询操作########################
concur = myset.find({}, {'_id':0})   #返回游标 遍历取值
# for i in concur:
#     print(i['name'], i['King'])

# for i in concur.limit(3):
    # print(i)

# for i in concur.sort([('King', 1)]):  #King表示按什么排序，1表示正序  与mongodb中不同之处
    # print(i)

# data = myset.find_one({'name':{'$gt':'张国立'}}, {'_id':0})
# print(data)   #返回字典

################################修改操作#########################
# myset.update_many({'King':'乾隆'}, {'$set':{'KingName':'玄烨'}}, upsert=True)
# myset.update({'King':'乾隆'}, {'$set':{'Kingname':'弘历'}}, multi=True)

################################删除操作#########################
# myset.delete_many({'age':{'$gt':20}})

################################其他操作#########################
# data = myset.find_one_and_delete({'age':{'$eq':19}})
# print(data)

################################索引操作##########################
# index = myset.create_index([('name', 1)])  #正向索引 返回值为索引名称
# print(index)
# for i in myset.list_indexes():
    # print(i)

###############################聚合操作###########################
l = [
    {'$group':{'_id':'$King', 'num':{'$sum':1}}},
    {'$sort':{'num':-1}}
]

consor = myset.aggregate(l)
for i in consor:
    print(i)

#关闭数据库连接
conn.close()
