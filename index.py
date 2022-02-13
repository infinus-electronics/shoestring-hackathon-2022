from dash import dcc
from dash import html
import dash

from app import app
from app import server
from layouts import shelves, inv, ana, heat
import callbacks


def serve_layout():

     print("layout")
     return html.Div([
          dcc.Location(id='url', refresh=True),
          html.Div(id='page-content'),
          dcc.Interval(
               id = "interval-component",
               interval= 30*1000,
               n_intervals = 0
          )
          # dcc.Button(id='invisible_button', style={'display':'none'})
     ])

app.layout = serve_layout

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
     print("callback")
     if pathname == '/apps/shelves-overview':
          return shelves
     elif pathname == '/apps/inv':
          return inv
     elif pathname == '/apps/ana':
          return ana
     elif pathname == '/apps/heat':
          return heat
     else:
          return shelves # This is the "home page"

# @app.routes("/apps/shelves-overview")
# def shelves():
#      return shelves

if __name__ == '__main__':
    app.run_server(debug=True, port = 1022)
