import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# from utils import compute_plot_gam
# from modeling import lrr, df, fb, col_map
# #from modeling import dfTrain, dfTrainStd, dfTest, dfTestStd, yTrain, yTest


# Compute the explanation dataframe, GAM, and scores
# xdf = lrr.explain().rename(columns={"rule/numerical feature": "rule"})
# xPlot, yPlot, plotLine = compute_plot_gam(lrr, df, fb, df.columns)
# train_acc = accuracy_score(yTrain, lrr.predict(dfTrain, dfTrainStd))
# test_acc = accuracy_score(yTest, lrr.predict(dfTest, dfTestStd))

def Header(name, app):
    title = html.H2(name, style={"margin-top": 5})
    logo = html.Img(
        src=app.get_asset_url("dash-logo.png"), style={"float": "right", "height": 50}
    )

    return dbc.Row([dbc.Col(title, md=9), dbc.Col(logo, md=3)])


train_acc = 10
test_acc = 10
total = train_acc + test_acc


#################################################################### Card componefe==defnts

cards = [
    dbc.Card(
        [
            html.H2(f"{train_acc:.2f}", className="card-title"),
            html.P("Item on shelf", className="card-text"),
        ],
        body=True,
        color="dark",
    ),
    dbc.Card(
        [
            html.H2(f"{test_acc:.2f}", className="card-title"),
            html.P("Item in Inventory", className="card-text"),
        ],
        body=True,
        color="dark",
        inverse=True,
    ),
    dbc.Card(
        [
            html.H2(f"{total:.2f}", className="card-title"),
            html.P("Item in Total", className="card-text"),
        ],
        body=True,
        color="dark",
    )
]




def get_cards():
    cards_num = dbc.Container(
    [
        html.Hr(),
        dbc.Row([dbc.Col(card) for card in cards]),
    ],
    fluid=False,
    )
    return cards_num
    
