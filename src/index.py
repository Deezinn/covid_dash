import dash
from dash import html, dcc, Input, Output, State

import dash_bootstrap_components as dbc

from app import *

from components.sidebar import sidebar
from pages import home, grafico_covid

app.layout = dbc.Container([
    dcc.Location(id='url'),
    dbc.Row([
        dbc.Col(sidebar, sm=1),
        dbc.Col(html.Div(id='page-content'), sm=11, style={'padding': '50px'}),
    ])
], fluid=True, style={"background-color": "black", 'position': 'fixed'})


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname == "/" or pathname == "/home":
        return home.layout
    elif pathname == "/graph-covid":
        return grafico_covid.layout

if __name__ == '__main__':
    app.run(debug=True)

