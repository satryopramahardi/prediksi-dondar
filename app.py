import dash
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

def import_table():
    df = pd.read_csv("data/blood.csv",sep=';')
    return df

df = import_table()

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="Demo",
    brand_href="#",
    sticky="top",
)

body = dbc.Container(
    [
        dbc.Row(
            [
                html.Div([
                    dcc.Upload(
                    id='unggah',
                    children=html.Div([
                        'Drag and Drop or ', html.A('Select Files')
                    ])
                )
                ], style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                )
            ],
            style={
                'width': '100%'
            }
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True,size='sm',responsive ='sm')
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(
                            figure={"data": [{"x": df.Month, "y": df.Donasi}]}
                        ),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = html.Div([navbar, body])

if __name__ == "__main__":
    app.run_server()
