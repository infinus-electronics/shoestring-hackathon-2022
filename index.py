import dash_core_components as dcc
import dash_html_components as html
import dash

from app import app
from app import server
from layouts import shelves, inv, page3
import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/shelves-overview':
         return shelves
    elif pathname == '/apps/inv':
         return inv
    elif pathname == '/apps/page3':
         return page3
    else:
        return shelves # This is the "home page"

if __name__ == '__main__':
    app.run_server(debug=True)
