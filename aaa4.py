import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
# server = app.server
app.config.suppress_callback_exceptions = True
app.title = 'Sistem Prediksi Donor Darah'