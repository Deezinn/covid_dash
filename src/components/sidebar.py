import dash
from dash import html, dcc, Input, Output, State

import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
from app import *


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 20,
    "bottom": 0,
    "width": "10rem",
    "padding": "2rem 1rem",
    "background-color": "black",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",

}

sidebar = dbc.Container(children=[
    html.Img(id='imagem-covid',src="assets/img/virus-icone.png", style={'width': '80px', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '20px'}),
    html.H6('SARS-CoV-2', className='dbc', style={'text-align': 'center', 'margin-top': '20px', 'color': 'white'}),
        html.Hr(style={'border': '1px solid #ccc', 'margin': '20px 0'}),
        dbc.Nav(
            [
            dbc.NavLink(
                "Início",
                href="/home",
                active="exact",
                className="custom-navlink"
            ),
            dbc.NavLink(
                "Gráficos",
                href="/graph-covid",
                active="exact",
                className="custom-navlink"
            ),
            ],
            vertical=True,
            pills=True,
        )
],style=SIDEBAR_STYLE)
