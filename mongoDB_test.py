from re import L
from .Collection_type import object_type

def create_test_collection(db_name, collection_name):
    dbname = object_type.get_db("test")
    collecton_name = dbname["test_collection"]


if __name__ == "__main__":
    create_test_collection()

