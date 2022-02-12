from gettext import install
from unicodedata import name
from pymongo import MongoClient
import pymongo


class object_type:
    def __init__(self, name, quantity, stock, batch_no, shelf, exp_date, is_exp):
        
        self.name = name
        if isinstance(name, list):
            self.name = name[0]
        self.quantity = quantity 
        self.stock = stock
        self.batch_no = batch_no
        self.shelf = shelf 
        self.exp_date = exp_date
        self.is_exp = is_exp
    


