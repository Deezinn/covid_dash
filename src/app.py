import dash
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.LUX,
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server
