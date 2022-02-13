from asyncio.base_tasks import _task_get_stack
from cgi import test
from re import L
import json 
from promotion_data import get_promotion_data
from .Collection_type import object_type
from pymongo import MongoClient
from .test_data import json_data

def get_db(name):
        
  connection_string = "mongodb://myUserAdmin:camjfl@13.40.33.147"
  client = MongoClient(connection_string)      
  return client["{}".format(name)]


def data_initialisation(): 
    test_data = json_data
    return test_data

def create_collection(db_name, collection_name):
  
  dbname = get_db("{}".format(db_name))
  collection = dbname["{}".format(collection_name)]

def promotion_func(): 
  data = get_promotion_data
  magnitude = []
  
  for i in data: 
    json_dict = json.loads(i)
    sum = 0
    for k in json_dict: 
      if json_dict[k].isdigit(): 
        sum += json_dict[k]
    
    magnitude.append(sum)
  return magnitude

def get_collection(db_name, col_name):
  db = get_db(db_name)
  col = db[col_name]
  return col 

def insert_into(col, json_dict):
  col.insert_many(json_dict)

def test_db_connection(db_name, col_name, data):
  col = get_collection(db_name, col_name)
  insert_into(col,data)

if __name__ == "__main__":
  do_something = 1

  #can try testing data initialisatioin 
