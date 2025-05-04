import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from app import app

sidebar = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/graph-covid/info1", active="exact"),
                dbc.NavLink("Page 1", href="/graph-covid/info2", active="exact"),
                dbc.NavLink("Page 2", href="/graph-covid/info3", active="exact"),
            ],
            vertical=False,
            pills=True,
        ),
    ],
    style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'justifyContent': 'center',
        'height': '100vh',
        'margin-top': 300,
        'padding': '20px',
    }
)
