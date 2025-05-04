from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from app import *
import plotly.graph_objs as go

from config.db import colecao

from app import app

from datetime import datetime
import time

layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.Img(src='assets/img/vomito.png', style={'width': '40px', 'margin': '10px'}),
                                html.H4('Sintomas', style={'color': 'black'}),
                                html.P('Tosse, Febre, falta de ar', style={'color': 'black'}),
                            ], style={'text-align': 'center'})
                        ], color='info', style={'border-radius': '20px', 'margin': '50px','top': '-40px'})
                    ]),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.Img(src='assets/img/localizacao-do-mapa.png', style={'width': '40px', 'margin': '10px'}),
                                html.H4('Origem', style={'color': 'black'}),
                                html.P('China', style={'color': 'black'}),
                            ], style={'text-align': 'center'})
                        ], color='success', style={'border-radius': '20px', 'margin': '50px','top': '-40px'})
                    ]),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.Img(src='assets/img/vacinado.png', style={'width': '40px', 'margin': '10px'}),
                                html.H4('Vacina', style={'color': 'black'}),
                                html.P('2020', style={'color': 'black'}),
                            ], style={'text-align': 'center'})
                        ], color='warning', style={'border-radius': '20px', 'margin': '50px','top': '-40px'})
                    ]),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.Img(src='assets/img/covid.png', style={'width': '40px', 'margin': '10px'}),
                                html.H4('Virus', style={'color': 'black'}),
                                html.P('SARS-CoV-2', style={'color': 'black'}),
                            ], style={'text-align': 'center'})
                        ], color='danger', style={'border-radius': '20px', 'margin': '50px','top': '-40px'})
                    ])
                ], style={'margin-top': '20px'})
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dbc.Row([
                            html.H4('Mortes por país', style={'text-align': 'center', 'margin-bottom': '20px'}),
                                dbc.Col([
                                    dcc.Dropdown(id='pais-dropdown', className='dbc',
                                    options=[],
                                    value='Brazil',
                                    placeholder='Selecione um país',
                                    style={'width': '80%', 'margin-top': '7px', 'margin-left': '80px'}
                                ),
                                ]),
                            ]),
                            dcc.Graph(id='morte-pais'),
                        ], style={'margin-top': '20px'}),
                        dbc.Col([
                            dbc.Row([
                                html.H4('Mortes por país', style={'text-align': 'center', 'margin-bottom': '20px'}),
                                dbc.Col([
                                    dcc.Dropdown(id='pais-dropdown2', className='dbc',
                                    options=[],
                                    value='Brazil',
                                    placeholder='Selecione um país',
                                    style={'width': '80%', 'margin-top': '7px', 'margin-left': '80px'}
                                ),
                                ]),
                            ]),
                            dcc.Graph(id='grafico-pizza', style={'margin-left': '340px', 'margin-top': '10px'})
                        ], style={'margin-top': '20px'}),
                    ])
                ]),
            ]),
            dbc.Row([
                dbc.Pagination(max_value=5, style={"justify-content":"center"})
            ])
        ]),

    ],
    fluid=True,
    style={
        'width': '100%',
        'height': '90vh',
        'background-color': 'white',
        'padding': '0px',
        'margin': '0',
        'border-radius': '20px'
    }
)

from dash import ctx

@app.callback(
    Output('pais-dropdown', 'options'),
    Output('pais-dropdown', 'value'),
    Input('pais-dropdown', 'id')
)
def carregar_paises(_):
    paises = colecao.distinct('pais')
    opcoes = [{'label': pais, 'value': pais} for pais in sorted(paises)]
    valor_padrao = 'Brazil' if 'Brazil' in paises else opcoes[0]['value']

    return opcoes, valor_padrao


@app.callback(
    Output('morte-pais', 'figure'),
    Input('pais-dropdown', 'value')
)
def atualizar_grafico(pais_selecionado):
    if not pais_selecionado:
        return go.Figure()

    data = colecao.find_one({'pais': pais_selecionado})
    if not data:
        return go.Figure()

    fig = go.Figure(data=[
        go.Bar(
            x=['Casos', 'Mortes', 'Recuperados', 'Testes'],
            y=[data['casos'], data['mortes'], data['recuperados'], data['testes']],
            marker=dict(color=['blue', 'red', 'green', 'orange']),
        )
    ])
    fig.update_layout(title=f'Dados de COVID-19 em {pais_selecionado}', height=400, title_x=0.5)

    return fig


@app.callback(
    Output('pais-dropdown2', 'options'),
    Output('pais-dropdown2', 'value'),
    Input('pais-dropdown2', 'id')
)
def carregar_paises(_):
    paises = colecao.distinct('pais')
    opcoes = [{'label': pais, 'value': pais} for pais in sorted(paises)]
    valor_padrao = 'Brazil' if 'Brazil' in paises else opcoes[0]['value']

    return opcoes, valor_padrao


@app.callback(
    Output('grafico-pizza', 'figure'),
    Input('pais-dropdown2', 'value')
)
def atualizar_grafico_pizza(pais_selecionado):
    if not pais_selecionado:
        return go.Figure()

    doc = colecao.find_one({'pais': pais_selecionado})
    if not doc:
        return go.Figure()

    ativos = doc.get('ativos', 0)
    recuperados = doc.get('recuperados', 0)
    mortes = doc.get('mortes', 0)

    fig = go.Figure(data=[
        go.Pie(
            labels=['Ativos', 'Recuperados', 'Mortes'],
            values=[ativos, recuperados, mortes],
            hole=0.4,
            marker=dict(colors=['#FFA500', '#00CC96', '#EF553B'])
        )
    ])
    fig.update_layout(
    width=300,
    height=400,
    title='Proporção dos casos',
    margin=dict(t=40, b=0, l=0, r=0)
    )

    return fig
