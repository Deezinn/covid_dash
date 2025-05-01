from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from app import *

layout = dbc.Container(fluid=True, style={'margin-top': '50px'}, children=[

    # Imagem de fundo com texto sobreposto
    dbc.Row([
        html.Div([
            html.Img(
                src='assets/testando.jpg',
                style={
                    'position': 'fixed',
                    'width': '500px',
                    'height': '1700px',
                    'transform': 'rotate(90deg)',
                    'margin-top': '-800px',
                    'margin-left': '760px'
                }
            ),

            html.Div(
                "SARS-CoV-2",
                style={
                    'position': 'fixed',
                    'top': '30px',
                    'left': '200px',
                    'width': '300px',
                    'color': 'white',
                    'font-size': '36px',
                    'font-weight': 'bold',
                    'background-color': 'black',
                    'text-align': 'center',
                    'padding': '15px'
                }
            ),

            html.Div(
                "Há uma hipótese sugere que o SARS-CoV-2 possa ter escapado de um laboratório em Wuhan, onde ao menos duas instituições — o Instituto de Virologia de Wuhan (WIV) e o Centro de Controle e Prevenção de Doenças de Wuhan (WHCDC).",
                style={
                    'position': 'fixed',
                    'top': '130px',
                    'left': '200px',
                    'width': '1000px',
                    'color': 'white',
                    'font-size': '28px',
                    'font-weight': 'bold',
                    'text-align': 'justify',
                    'white-space': 'normal',
                    'word-wrap': 'break-word',
                    'background-color': 'rgba(0, 0, 0, 0.2)',
                    'padding': '20px'
                }
            ),
        ], style={'position': 'relative'})
    ]),

    # Texto explicativo abaixo da imagem
    dbc.Row([
        html.Div(
            "A Covid-19 é uma infecção respiratória grave causada pelo vírus Sars-Cov-2. Sua taxonomia científica pertence à família Coronaviridae, subgênero Sarbecovírus. Estudos mostram que vírus como o SARS e o MERS são de origem zoonótica. Com relação ao SARS-CoV-2, acredita-se que o surto inicial esteja ligado ao mercado de frutos do mar de Huanan, em Wuhan, local onde eram vendidas diversas espécies de animais silvestres. Acredita-se que esse ambiente pode ter propiciado o salto do vírus de animais para humanos.",
            style={
                'margin-top': '380px',
                'margin-left': '160px',
                'color': 'black',
                'font-size': '26px',
                'font-weight': 'normal',
                'width': '1750px',
                'text-align': 'justify',
                'position': 'fixed'
            }
        )
    ]),

    # Rodapé com colunas de exemplo
    dbc.Row([
        dbc.Col([
            html.Img(
                src='assets/virus.png',
                style={'margin-left': '100px', 'width': '300px'}
            )
        ]),
        dbc.Col([
            html.Div(
                "Relatos iniciais indicam que os primeiros infectados tiveram contato com o mercado de Huanan, reforçando a hipótese de transmissão animal-humano. Estudos genéticos indicam que morcegos são os prováveis hospedeiros naturais, enquanto animais intermediários, como o pangolim, podem ter facilitado a transmissão para humanos. Essa teoria é sustentada por semelhanças genéticas entre os vírus encontrados nesses animais e o SARS-CoV-2, ainda que mais investigações sejam necessárias.",
                style={
                    'color': 'black',
                    'font-size': '24px',
                    'width': '1000px',
                    'margin-left': '450px',
                    'text-align': 'justify',
                    'position': 'fixed'
                }
            )
        ])
    ], style={
        'margin-top': '650px',
        'margin-left': '150px',
        'position': 'fixed'
    })
])
