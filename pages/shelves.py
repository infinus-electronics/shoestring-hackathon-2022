from webbrowser import get
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import dash
import dash_table
from dash_table.Format import Format, Group
import dash_table.FormatTemplate as FormatTemplate
from datetime import datetime as dt
# from app import app

from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://myUserAdmin:camjfl@13.40.33.147:27017")
db = client.admin
col = db["Milk 1L"]

excludes = ['system.version', 'system.users', 'Discounts', 'Starbucks House Blend', 'Durian Ice Cream']

# serverStatusResult=db.command("serverStatus")
pprint(db.list_collection_names())

from pages.header import get_header
from pages.navbar import get_navbar
from pages.emptybar import get_emptyrow

corporate_colors = {
    'dark-blue-grey' : 'rgb(62, 64, 76)',
    'medium-blue-grey' : 'rgb(77, 79, 91)',
    'superdark-green' : 'rgb(41, 56, 55)',
    'dark-green' : 'rgb(57, 81, 85)',
    'medium-green' : 'rgb(93, 113, 120)',
    'light-green' : 'rgb(186, 218, 212)',
    'pink-red' : 'rgb(255, 101, 131)',
    'dark-pink-red' : 'rgb(247, 80, 99)',
    'white' : 'rgb(251, 251, 252)',
    'light-grey' : 'rgb(208, 206, 206)'
}

externalgraph_rowstyling = {
    'margin-left' : '15px',
    'margin-right' : '15px'
}

externalgraph_colstyling = {
    'border-radius' : '10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['superdark-green'],
    'background-color' : corporate_colors['superdark-green'],
    'box-shadow' : '0px 0px 17px 0px rgba(186, 218, 212, .5)',
    'padding-top' : '10px'
}

filterdiv_borderstyling = {
    'border-radius' : '0px 0px 10px 10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['light-green'],
    'background-color' : corporate_colors['light-green'],
    'box-shadow' : '2px 5px 5px 1px rgba(255, 101, 131, .5)'
    }

navbarcurrentpage = {
    'text-decoration' : 'underline',
    'text-decoration-color' : corporate_colors['pink-red'],
    'text-shadow': '0px 0px 1px rgb(251, 251, 252)'
    }

recapdiv = {
    'border-radius' : '10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : 'rgb(251, 251, 252, 0.1)',
    'margin-left' : '15px',
    'margin-right' : '15px',
    'margin-top' : '15px',
    'margin-bottom' : '15px',
    'padding-top' : '5px',
    'padding-bottom' : '5px',
    'background-color' : 'rgb(251, 251, 252, 0.1)'
    }

recapdiv_text = {
    'text-align' : 'left',
    'font-weight' : '350',
    'color' : corporate_colors['white'],
    'font-size' : '1.5rem',
    'letter-spacing' : '0.04em'
    }

####################### Corporate chart formatting

corporate_title = {
    'font' : {
        'size' : 16,
        'color' : corporate_colors['white']}
}

corporate_xaxis = {
    'showgrid' : False,
    'linecolor' : corporate_colors['light-grey'],
    'color' : corporate_colors['light-grey'],
    'tickangle' : 315,
    'titlefont' : {
        'size' : 12,
        'color' : corporate_colors['light-grey']},
    'tickfont' : {
        'size' : 11,
        'color' : corporate_colors['light-grey']},
    'zeroline': False
}

corporate_yaxis = {
    'showgrid' : True,
    'color' : corporate_colors['light-grey'],
    'gridwidth' : 0.5,
    'gridcolor' : corporate_colors['dark-green'],
    'linecolor' : corporate_colors['light-grey'],
    'titlefont' : {
        'size' : 12,
        'color' : corporate_colors['light-grey']},
    'tickfont' : {
        'size' : 11,
        'color' : corporate_colors['light-grey']},
    'zeroline': False
}

corporate_font_family = 'Dosis'

corporate_legend = {
    'orientation' : 'h',
    'yanchor' : 'bottom',
    'y' : 1.01,
    'xanchor' : 'right',
    'x' : 1.05,
	'font' : {'size' : 9, 'color' : corporate_colors['light-grey']}
} # Legend will be on the top right, above the graph, horizontally

corporate_margins = {'l' : 5, 'r' : 5, 't' : 45, 'b' : 15}  # Set top margin to in case there is a legend

corporate_layout = go.Layout(
    font = {'family' : corporate_font_family},
    title = corporate_title,
    title_x = 0.5, # Align chart title to center
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
    xaxis = corporate_xaxis,
    yaxis = corporate_yaxis,
    height = 270,
    legend = corporate_legend,
    margin = corporate_margins
    )

shelf_grid = {

    "display": "grid",
    "grid-template-columns": "repeat(3, 1fr)",
    "gap": "10px",
    "grid-auto-rows": "minmax(100px, auto)",
}

box = {
  "background-color": "#444",
  "color": "#fff",
  "border-radius": "5px",
  "padding":"20px",
#   "font-size": "150%",
}

def shelves():

    items = db.list_collection_names()

    thisTable = []
    for i in range(1, 10): #numrows
        thisCol = []
        for j in ['A', 'B', 'C']: #numcols

            cell = html.Div([

                        html.Div(["{}{}".format(str(j), str(i))], className = "p-3 border bg-primary text-center")

                    ], className = "col")

            for item in items:

                if item in excludes:
                    continue
                pprint(item)
                collection = db[item].find()
                # for k in collection:
                #     pprint(k)
                # pprint(collection[0])
                
                shelf = collection[0]['shelf']
                shelf = [c for c in shelf]

                if shelf[0] == j and shelf[1] == str(i):

                    thisProductCount = 0
                    for lot in collection:
                        thisProductCount = thisProductCount + int(lot['on_display'])

                    if thisProductCount == 0:

                        cell = html.Div([

                            html.Div(["{}{}: {}, {} left".format(str(j), str(i), str(item), str(thisProductCount))], className = "p-3 border bg-danger text-center")

                        ], className = "col")

                    elif thisProductCount <= 5:

                        cell = html.Div([

                            html.Div(["{}{}: {}, {} left".format(str(j), str(i), str(item), str(thisProductCount))], className = "p-3 border bg-warning text-center")

                        ], className = "col")

                    else:

                        cell = html.Div([

                            html.Div(["{}{}: {}, {} left".format(str(j), str(i), str(item), str(thisProductCount))], className = "p-3 border bg-success text-center")

                        ], className = "col")

            thisCol.append(cell)

        thisTable.append(html.Div(thisCol, className="row g-2"))

    



    page = ([#####################
    #Row 1 : Header
    get_header(),

    #####################
    #Row 2 : Nav bar
    get_navbar('Shelves'),
    
    get_emptyrow(),
    #####################
    #Row 3 : Filters

    

    html.Div(thisTable, className = "container")
    
       

    ])
    return page



