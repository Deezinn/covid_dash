import dash
from dash import html, dcc, Input, Output, State

import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
from app import *

app.layout = dbc.Container(children=[
    dcc.Location(id='url'),
    html.Div(id='page-content')
], fluid=True)

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname == "/" or pathname == "/home":
        pass

if __name__ == '__main__':
    app.run(debug=True)
