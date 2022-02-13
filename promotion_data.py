"""
This module is not used
"""

import json
from mongoDB_test import get_db
from pymongo import MongoClient
import pymongo


def get_promotion_data():
  db = get_db("admin")
  promotion_data = db["Discounts"]
  return json(promotion_data)
