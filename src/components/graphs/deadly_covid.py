import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

deadly = dbc.Container(
   children=[
      dbc.Row([
         dbc.Col([
            dcc.Graph()
         ])
      ])
   ]
)
