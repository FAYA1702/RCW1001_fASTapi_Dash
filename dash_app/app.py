import dash
from dash import html, dcc

# Initialiser l'application Dash
app = dash.Dash(__name__, requests_pathname_prefix='/dashboard/')

# Layout de l'application
app.layout = html.Div(children=[

    # Navigation
    html.Div([
        html.A('Accueil', href='/'),
        " | ",
        html.A('Logout', href='/logout'),
    ], style={'marginTop': '25px'}),

    html.H1("Dashboard avec FastAPI + Dash"),

    # === LINE GRAPH ===
    html.H2("**** Line Graph ***"),
    dcc.Graph(
        id='exm1',
        figure={
            "data": [
                {"x": [1, 3, 5], "y": [10, 12, 14], "type": "line", "name": "exemple1"},
                {"x": [2, 4, 6], "y": [13, 15, 17], "type": "line", "name": "exemple2"},
            ]
        }
    ),

    # === SCATTER GRAPH ===
    html.H2("**** Scatter Plot Graph ***"),
    dcc.Graph(
        id='exm2',
        figure={
            "data": [
                {"x": [1, 3, 5, 7], "y": [10, 12, 14, 16], "type": "scatter", "mode": "markers", "name": "scatter exemple1"},
                {"x": [2, 4, 6, 8], "y": [13, 15, 17, 19], "type": "scatter", "mode": "markers", "name": "scatter exemple2"},
            ]
        }
    ),

    # === PIE CHART ===
    html.H2("**** Pie Chart Graph ***"),
    dcc.Graph(
        id='exm3',
        figure={
            "data": [
                {
                    "labels": ["A", "B", "C"],
                    "values": [10, 12, 14],
                    "type": "pie",
                    "name": "pie chart exemple"
                }
            ],
            "layout": {
                "title": "Répartition en secteurs"
            }
        }
    )
])

# Pour l'intégration avec FastAPI
server = app.server
