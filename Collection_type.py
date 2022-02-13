from gettext import install
from unicodedata import name
from pymongo import MongoClient
import pymongo
import datetime


class object_type:
    def __init__(self, in_storage, on_display, lot_number, mass_per_item, shelf, expiry_date):
        
        self.on_display = on_display 
        self.in_storage = in_storage
        self.lot_number = lot_number
        self.shelf = shelf 
        self.expiry_date = expiry_date
        self.mass_per_item = mass_per_item
    
    def create_json_item(self):
        dict = {"expiry date" : datetime(self.expiry_date),
                "in_storage" : int(self.in_storage),
                "on_display" : int(self.on_display),
                "lot_number" : str(self.lot_number),
                "shelf" : str(self.shelf),
                "mass_per_item" : int(self.mass_per_item)
                }
                
    


