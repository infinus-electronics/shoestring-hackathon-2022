import dash
import pathlib
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from plotly import tools
import plotly.express as px
from pymongo import MongoClient
from pprint import pprint
import datetime
client = MongoClient("mongodb://myUserAdmin:camjfl@13.40.33.147:27017")
db = client.trend_history
values = db["load_values"]
record = values.find().sort([('_id', -1)]).limit(100)

# pprint(values)
excludes = ['system.version', 'system.users', 'Discounts']
# pprint(record)
# serverStatusResult=db.command("serverStatus")
# pprint(db.list_collection_names())


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# def create_df():
#     # intialise data of lists.
#     data = {'Name': ['Nick hospital', 'Nick hospital', 'Nick hospital', 'Krish hospital', 'Krish hospital',
#                      'Krish hospital'],
#             'NAR_forms_used': [2, 1, 2, 2, 2, 3]}

#     # Create DataFrame
#     return data

y = [string["weight"] for string in record]
y = y[::-1]
# y = y[-20:-1]

record = values.find().sort([('_id', -1)]).limit(100)

# pprint(record[0])
uniq_x = [string["time"] for string in record]
# pprint(uniq_x)
x =[]

for item in uniq_x:
   x.append(datetime.datetime.fromtimestamp(item))
x = x[::-1]
# x = x[-20:-1]
# def create_figure( df):
#     # set up plotly figure
#     fig =  px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
#     return fig
pprint(x)
fig = px.line(x = x, y =y, title ='Graph of Weight against Time' )
fig.update_yaxes(range = [0,5500])



def get_graph():
    graph = html.Div([
        dcc.Graph(figure = fig)
        
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
    