from gettext import install
from unicodedata import name
from pymongo import MongoClient
import pymongo


class object_type:
    def __init__(self, name, quantity, stock, batch_no, shelf, exp_date):
        
        self.name = name
        if isinstance(name, list):
            self.name = name[0]
        self.quantity = quantity 
        self.stock = stock
        self.batch_no = batch_no
        self.shelf = shelf 
        self.exp_date = exp_date
    
    def get_db(self, name):
        
        connection_string = "mongodb://myUserAdmin:camjfl@13.40.33.147"
        client = MongoClient(connection_string)
        
        return client["{}".format(name)]




