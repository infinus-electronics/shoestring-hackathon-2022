import sys
from dash import Dash, Input, Output, callback, dash_table
import pandas as pd
import dash_bootstrap_components as dbc
from pymongo import MongoClient
from pprint import pprint
import pymongo
from pandas.io.json import json_normalize

client = MongoClient("mongodb://myUserAdmin:camjfl@13.40.33.147:27017")
db = client.admin
col = db["Milk 1L"]
datapoints = pd.DataFrame(list(col.find()))
df = json_normalize(datapoints)
df.head()

# print(col)

# milk_num = []
# for list in col:
#     for element in list:
#         milk_batch = []
#         milk_batch.append(j)
#     milk_num.append(milk_batch)
    


# select the collection within the database
# test = db.test
# convert entire collection to Pandas dataframe
# test = pd.DataFrame(list(test.find()))

# df = pd.read_json(path_or_buf="file_path\json.txt",  typ='frame')

df = pd.read_csv('pages\page_2_inventory\tablehack.csv')


table = dbc.Container([
    dbc.Label('Click a cell in the table:'),
    dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], id='tbl'),
    dbc.Alert(id='tbl_out'),
])

@callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"