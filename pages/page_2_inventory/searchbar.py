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
df = pd.read_csv(DATA_PATH.joinpath("small_molecule_drugbank.csv")).drop(
    ["Unnamed: 0"], axis=1
)
def get_searchbar():
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
                            options=[{"label": i, "value": i} for i in df["NAME"]],
                        )
                    ],
                    className="app__dropdown",
                ),
            ]
        ) 
    ]
    )
    return searchbar