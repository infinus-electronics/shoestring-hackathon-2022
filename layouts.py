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
from app import app

import pages.shelves as shelves
import pages.page_2_inventory.inv as inv
import pages.page_3_analysis.ana as ana
import pages.heat as heat

from pages.navbar import get_navbar
from pages.header import get_header
from pages.emptybar import get_emptyrow

####################################################################################################
# 000 - FORMATTING INFO
####################################################################################################

####################### Corporate css formatting
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

####################################################################################################
# 000 - DATA MAPPING
####################################################################################################

#Sales mapping
sales_filepath = 'data/datasource.xlsx'

sales_fields = {
    'date' : 'Date',
    'reporting_group_l1' : 'Country',
    'reporting_group_l2' : 'City',
    'sales' : 'Sales Units',
    'revenues' : 'Revenues',
    'sales target' : 'Sales Targets',
    'rev target' : 'Rev Targets',
    'num clients' : 'nClients'
    }
sales_formats = {
    sales_fields['date'] : '%d/%m/%Y'
}

####################################################################################################
# 000 - IMPORT DATA
####################################################################################################

###########################
#Import sales data
xls = pd.ExcelFile(sales_filepath)
sales_import=xls.parse('Static')

#Format date field
sales_import[sales_fields['date']] = pd.to_datetime(sales_import[sales_fields['date']], format=sales_formats[sales_fields['date']])
sales_import['date_2'] = sales_import[sales_fields['date']].dt.date
min_dt = sales_import['date_2'].min()
min_dt_str = str(min_dt)
max_dt = sales_import['date_2'].max()
max_dt_str = str(max_dt)

#Create L1 dropdown options
repo_groups_l1 = sales_import[sales_fields['reporting_group_l1']].unique()
repo_groups_l1_all_2 = [
    {'label' : k, 'value' : k} for k in sorted(repo_groups_l1)
    ]
repo_groups_l1_all_1 = [{'label' : '(Select All)', 'value' : 'All'}]
repo_groups_l1_all = repo_groups_l1_all_1 + repo_groups_l1_all_2

#Initialise L2 dropdown options
repo_groups_l2 = sales_import[sales_fields['reporting_group_l2']].unique()
repo_groups_l2_all_2 = [
    {'label' : k, 'value' : k} for k in sorted(repo_groups_l2)
    ]
repo_groups_l2_all_1 = [{'label' : '(Select All)', 'value' : 'All'}]
repo_groups_l2_all = repo_groups_l2_all_1 + repo_groups_l2_all_2
repo_groups_l1_l2 = {}
for l1 in repo_groups_l1:
    l2 = sales_import[sales_import[sales_fields['reporting_group_l1']] == l1][sales_fields['reporting_group_l2']].unique()
    repo_groups_l1_l2[l1] = l2

################################################################################################################################################## SET UP END

####################################################################################################
# 000 - DEFINE REUSABLE COMPONENTS AS FUNCTIONS
####################################################################################################



shelves = shelves.shelves()

####################################################################################################
# 002 - Page 2
####################################################################################################

inv = inv.inv()


####################################################################################################
# 003 - Page 3
####################################################################################################

ana = ana.ana()

heat = heat.heat()
