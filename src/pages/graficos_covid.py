from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from app import *
import plotly.graph_objs as go

from config.db import colecao

from app import app


import pandas as pd
import plotly.express as px

layout = dbc.Container(
   children=[
      html.H1(id='', className='', children='teste')
   ]
)
