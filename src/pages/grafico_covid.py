from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from app import *
import plotly.graph_objs as go

from config.db import colecao

from app import app

from components import options_graph
from components.graphs import deadly_covid
def layout(pathname):
    return dbc.Container(
        children=[
            dbc.Row([
                html.Div(render_subpage(pathname), id='page-content-graph', style={'margin-top': '20px'}),
            ]),
            dbc.Row([
                dbc.Col([
                    options_graph.sidebar,
                ])
            ])
        ],
        fluid=True,
        style={
            'width': '100%',
            'height': '90vh',
            'background-color': 'white',
            'padding': '0px',
            'border-radius': '20px'
        }
    )

def render_subpage(pathname):
    if pathname == "/graph-covid" or pathname == "/graph-covid/info1":
        return deadly_covid.deadly
    elif pathname == "/graph-covid/info2":
        return html.P("This is the content of page 2. Yay!", style={'background-color': 'red'})
    elif pathname == "/graph-covid/info3":
        return html.P("Oh cool, this is page 3!", style={'background-color': 'blue'})
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )
