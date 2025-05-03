from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

layout = dbc.Container(
    children=[
        html.H1(id='titulo-home', className='dbc', children='Informação', style={'padding': '20px'}),
        html.P(id='', className='', children='teste', style={'padding-left': '20px'}),
        html.Img(src='assets/img/virus.jpg', style={'width': '40%', 'height': '100%', 'border-radius': '20px', 'position': 'absolute', 'right': '0', 'top': '0'})
    ],
    fluid=True,
    style={
        'width': '100%',
        'height': '90vh',
        'background-color': 'white',
        'padding': '0px',
        'margin': '0',
        'border-radius': '20px',
        'position': 'relative'
    }
)
