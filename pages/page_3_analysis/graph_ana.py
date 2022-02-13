import dash
import pathlib
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from plotly import tools
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def create_df():
    # intialise data of lists.
    data = {'Name': ['Nick hospital', 'Nick hospital', 'Nick hospital', 'Krish hospital', 'Krish hospital',
                     'Krish hospital'],
            'NAR_forms_used': [2, 1, 2, 2, 2, 3]}

    # Create DataFrame
    df = pd.DataFrame(data)

    
    

    return df

def create_figure( df):
    # set up plotly figure
    fig =  px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
    return fig

def get_graph():
    graph = html.Div([
        dcc.Graph(id='graph', figure=create_figure(create_df())),
        dcc.Dropdown(
                    id="Hosp_list",
                    options=[{"label": i, "value": i} for i in create_df()['Name'].tolist()],
                    multi=True,
                    value=list(),

            )
    ])

    @app.callback(
        Output('graph', 'figure'),
        [Input('Hosp_list', 'value') ])
    def dropdown_changed(values):
        # TODO:
        # build a graph depending on the dropdown selection (parameter values) and
        # return it instead of dash.no_update (which prevents update of client)
        print('Dropdown triggered with these values:', values)
        return dash.no_update
    return graph
    s