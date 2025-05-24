from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from app import *
import plotly.graph_objs as go

from config.db import colecao

from app import app


import pandas as pd
import plotly.express as px


data = pd.DataFrame({
    'country': ['Brazil', 'Germany', 'India', 'China', 'USA'],
    'continent': ['South America', 'Europe', 'Asia', 'Asia', 'North America'],
    'pop': [213_000_000, 83_000_000, 1_366_000_000, 1_412_000_000, 331_000_000]
})

layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='graph-map')
            ])
        ]),
        ],
        fluid=True,
        style={
            'margin-top': '100px'
        }
)


@app.callback(
    Output('graph-map', 'figure'),
    Input('graph-map', 'id')
)
def update_graph_map(_):
    fig = px.scatter_geo(
    data,
    locations="country",
    locationmode='country names',
    color="continent",
    hover_name="country",
    size="pop",
    projection="natural earth",
    title="Mapa Simulado com Dados Fictícios"
    )
    return fig
