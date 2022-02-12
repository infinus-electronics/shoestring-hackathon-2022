from re import L
from .Collection_type import object_type

def create_test_collection(db_name, collection_name):
    dbname = object_type.get_db("{}".format(db_name))
    collecton_name = dbname["{}".format(collection_name)]

def insert_docs():
    s = 1
    

if __name__ == "__main__":
    create_test_collection("test","test_c")

