import dash_bootstrap_components as dbc
from dash import html

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("A covid...", className="card-text"),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button('teste')
        ]
    ),
    className="mt-3",
)
