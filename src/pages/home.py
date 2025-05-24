from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

from components.tabs import tab1_content, tab2_content
from app import app

layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.Div([
                        html.Div([
                            html.Img(
                                src='assets/img/virus-header.png',
                                style={
                                    'width': '100%',
                                    'height': '35vh',
                                    'object-fit': 'cover',
                                    'border-radius': '10px 10px 10px 10px'
                                }
                            )
                        ], style={'position': 'relative'}),
                        html.Div([
                            html.H1(children='Sars-Cov-2', style={'color': 'white', 'font-family': 'roboto, sans-serif, arial, helvetica'}),
                            html.P(children='Há uma hipótese sugere que o SARS-CoV-2 possa ter escapado de um laboratório em Wuhan, onde ao menos duas instituições — o Instituto de Virologia de Wuhan (WIV) e o Centro de Controle e Prevenção de Doenças de Wuhan (WHCDC) ', style={'color': 'white', 'font-size': '18px', 'font-family': 'roboto, sans-serif, arial, helvetica'})
                        ], style={
                            'position': 'absolute',
                            'top': '8vh',
                            'left': '45%',
                            'zIndex': '1',
                            'color': 'white',
                            'justify-content': 'flex-end',
                            'padding': '16px',
                            'max-width': '50%',
                            'text-align': 'right'

                        }),
                    ],style={'display': 'flex-box', 'align-items': 'center'})
                ]),
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        dbc.Row([
                            html.H1(id='', className='', children='O que é a covid?', style={'color': '#00006B', 'font-family': '"roboto", sans-serif, arial, helvetica', 'padding-top': '10px', 'padding-left': '32px'})
                        ]),
                        dbc.Row([
                            html.P('A Covid-19 é uma infecção respiratória grave causada pelo vírus Sars-Cov-2. Sua taxonomia científica pertence a família Coronaviridae, subgênero Sarbecovírus. Os vírus SARS e MERS, são predominantemente de origem zoonótica. No caso do SARS-CoV-2, observou-se associação inicial com o mercado atacadista de frutos do mar de Huanan, em Wuhan, onde eram comercializadas diversas espécies de animais silvestres.',style={'font-family': '"roboto", sans-serif, arial, helvetica', 'padding-left': '32px'})
                        ])
                    ],sm=6),
                    dbc.Col([
                        html.Img(src='assets/img/mapa.png', style={'width': '500px', 'border-radius': '10px', 'display': 'block', 'margin-top': '50px', 'object-fit': 'contain', 'margin-left': '200px'})
                    ],sm=6)
                ]),
                dbc.Row([
                    dbc.Col([
                        html.Img(src='assets/img/menino-mascara.png', style={'width': '500px', 'border-radius': '10px', 'display': 'block', 'margin': '-120px 180px'})
                    ],sm=6),
                    dbc.Col([
                        dbc.Row([
                            html.P('Relatos de que os primeiros pacientes frequentaram esse mercado reforçaram a hipótese de transmissão animal-humano. Estudos genéticos indicam que morcegos são os prováveis hospedeiros naturais, com possibilidade de um hospedeiro intermediário, como o pangolim, ter facilitado o salto interespecífico do vírus para humanos.',style={'font-family': '"roboto", sans-serif, arial, helvetica', 'text-align': 'right', 'padding-right': '32px', 'margin-top': '50px'})
                        ], style={'margin-top': '0'})
                    ],sm=6),
                ], style={})
            ],style={'background-color': 'white'})
        ], style={'width': '98%', 'height': 'auto', 'margin-left': '18px', 'margin-top': '40px'})
    ],
    fluid=True,
    style={
        'width': '100%',
        'height': '90vh',
        'padding': '0px',
        'margin-top': '12px',
        'position': 'relative',
    }
)
