import pymongo
import pprint


client = pymongo.MongoClient("mongodb://myUserAdmin:camjfl@13.40.33.147:27017")
db = client.admin
col = db["Milk 1L"]

excludes = ['system.version', 'system.users', 'Discounts']

# serverStatusResult=db.command("serverStatus")
pprint(db.list_collection_names())