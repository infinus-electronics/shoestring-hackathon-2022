from pymongo import MongoClient
from pprint import pprint
import json
import warnings
warnings.filterwarnings('ignore')

client = MongoClient("mongodb://myUserAdmin:camjfl@13.40.33.147:27017")
db = client.admin


# serverStatusResult=db.command("serverStatus")
pprint(db.list_collection_names())