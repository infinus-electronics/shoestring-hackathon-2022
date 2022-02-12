from asyncio.base_tasks import _task_get_stack
from cgi import test
from re import L
import json 
from promotion_data import promotion_data
from .Collection_type import object_type
from pymongo import MongoClient
from .test_data import json_data

def get_db(name):
        
  connection_string = "mongodb://myUserAdmin:camjfl@13.40.33.147"
  client = MongoClient(port = connection_string)      
  return client["{}".format(name)]


def data_initialisation(): 
    test_data = json_data
    return test_data

def create_collection(db_name, collection_name):
  
  dbname = get_db("{}".format(db_name))
  collection = dbname["{}".format(collection_name)]

def insert_docs(db, collection_name, data):
  
  obj_list = []
  with data as f: 
    for jsonObject in f: 
      obj_dict = json.loads(jsonObject) 
      obj_list.append(obj_dict)
  db[collection_name].insert_many(obj_list)

def promotion_func(): 
  data = promotion_data
  magnitude = []
  
  for i in data: 
    json_dict = json.loads(i)
    sum = 0
    for k in json_dict: 
      if json_dict[k].isdigit(): 
        sum += json_dict[k]
    
    magnitude.append(sum)
  return magnitude

if __name__ == "__main__":
  db_name = "test"
  c_name = "test_c"
  data = data_initialisation()
  
  get_db(db_name)
  create_collection(db_name, c_name)
  insert_docs(db_name, c_name, data)

  #can try testing data initialisatioin 
