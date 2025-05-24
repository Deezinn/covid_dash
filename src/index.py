import dash
from dash import html, dcc, Input, Output, State

import dash_bootstrap_components as dbc

from app import *

from components.sidebar import sidebar
from pages import home
from pages import mapa_covid, graficos_covid

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    dbc.Row([
        dbc.Col(sidebar, sm=1),
        dbc.Col(html.Div(id='page-content'), sm=11),
    ])

], fluid=True)


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname.startswith("/graph-covid"):
        return mapa_covid.layout
    elif pathname == "/" or pathname == "/home":
        return home.layout
    elif pathname == "/graph-chart-covid":
        return graficos_covid.layout
    else:
        return html.Div("404 Página não encontrada")

if __name__ == '__main__':
    app.run(debug=True)

