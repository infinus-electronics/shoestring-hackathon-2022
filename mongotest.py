from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://myUserAdmin:camjfl@13.40.33.147:27017", )
db = client.admin
col = db["Milk 1L"]


excludes = ['system.version', 'system.users', 'Discounts', 'Starbucks House Blend', 'Durian Ice Cream']

items = db.list_collection_names()

for item in items:
    if item in excludes:
        continue
    pprint(item)

# pprint(items[4])

    collection = db[item].find()

    pprint(collection[0])

# for k in collection:
#     pprint(k)
#     pprint(k['shelf'])