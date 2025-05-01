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
    "left": 10,
    "bottom": 0,
    "width": "8rem",
    "padding": "2rem 1rem",
    "background-color": "#7f7f7f",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",

}

sidebar = dbc.Container(children=[
    html.Img(id='imagem-covid',src="assets/virus.png", disable_n_clicks=True, style={'width': '80px', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
        html.Hr(style={'border': '1px solid #ccc', 'margin': '20px 0'}),
        dbc.Nav(
            [
                html.A(
                    html.Img(src="assets/botao-home.png", disable_n_clicks=True, style={'width': '40px', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '50px'}),
                    href="/"
                ),
                html.A(
                    html.Img(src="assets/estatisticas.png", disable_n_clicks=True, style={'width': '40px', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '80px'}),
                    href="/graph-covid"
                ),html.A(
                    #ainda nao sei oq colocar
                ),
            ],
            vertical=True,
            pills=True,
        )
],style=SIDEBAR_STYLE)
