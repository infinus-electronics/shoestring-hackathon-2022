import dash
import pathlib
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from plotly import tools
app = dash.Dash(__name__, suppress_callback_exceptions=True)
DATA_PATH = pathlib.Path(__file__).parent.joinpath("data").resolve()
STARTING_DRUG = "Durian Maggi"
# df = pd.read_csv(DATA_PATH.joinpath("small_molecule_drugbank.csv")).drop(
#     ["Unnamed: 0"], axis=1
# )

from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://myUserAdmin:camjfl@13.40.33.147:27017")
db = client.admin
name = []

def get_searchbar():
    name = db.list_collection_names()
    excludes = ['system.version', 'system.users', 'Discounts']
    name = [c for c in name if c not in excludes]
    searchbar = html.Div(
    [
        
        html.Div(
            [
                
                html.Div(
                    [
                        dcc.Dropdown(
                            id="chem_dropdown",
                            multi=True,
                            value=[STARTING_DRUG],
                            options=[{"label": i, "value": i} for i in name],
                        )
                    ],
                    className="app__dropdown",
                ),
            ]
        ) 
    ]
    )
    return searchbar