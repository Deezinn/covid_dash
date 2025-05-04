from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

from components.tabs import tab1_content, tab2_content
from app import app

layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([
                html.H1(id='titulo-home', className='dbc', children='Informação', style={'padding': '20px'}),
                dbc.Row([
                    dbc.Col([
                        html.P(id='', className='', children='teste', style={'padding-left': '20px'}),
                    ])
                ]),
                dbc.Row([
                    dbc.Col([
                dbc.Tabs([
                    dbc.Tab(label="tab 1", tab_id='tab-1'),
                    dbc.Tab(label="tab 2", tab_id='tab-2')
                ],
                id='tabs',
                active_tab='tab-1'
                ),
                    html.Div(id='content')
                    ])
                ])
            ]),

        ]),
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

@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return tab1_content
    elif at == "tab-2":
        return tab2_content

