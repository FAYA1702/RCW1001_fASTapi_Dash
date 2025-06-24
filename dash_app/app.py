import dash
from dash import html, dcc
import requests

#  Fonction pour récupérer la météo depuis une API externe http://127.0.0.1:8001/info
def fetch_weather_info():
    try:
        response = requests.get("http://rcw1002-projet-2-hjgzchcbayepbbfe.canadacentral-01.azurewebsites.net/info", timeout=2)
        return response.json()  # ✅ Cette ligne manquait !
    except Exception as e:
        print("Erreur météo:", e)
        return {
            "date": "N/A",
            "time": "N/A",
            "weather": {
                "city": "N/A",
                "temperature": "N/A",
                "description": "N/A"
            }
        }


#  Récupération des données météo
weather_info = fetch_weather_info()

#  Initialisation de l'application Dash
app = dash.Dash(__name__, requests_pathname_prefix='/dashboard/')

#  Layout principal
app.layout = html.Div(children=[

    # Barre de navigation
    html.Div([
        html.A('Accueil', href='/'),
        " | ",
        html.A("Logout", href="/logout")
    ], style={'marginTop': 25}),

    html.H1(children="Exemple de Dashboard"),

    #  Bloc météo
    html.Div([
        html.H3("Informations météo"),
        html.P(f"Aujourd'hui est le {weather_info['date']} à {weather_info['time']}"),
        html.P(f"Ville : {weather_info['weather']['city']}"),
        html.P(f"Température : {weather_info['weather']['temperature']} °C"),
        html.P(f"Description : {weather_info['weather']['description']}"),
    ], style={"margin": "20px 0"}),

    # Graphiques
    html.H2("*** Bar Graph *** "),
    dcc.Graph(
        id="exm1",
        figure={
            "data": [
                {"x": [5, 7, 12], "y": [10, 16, 11], "type": "bar", "name": "exmple1"},
                {"x": [8, 18, 22], "y": [5, 8, 3], "type": "bar", "name": "exmple2"}
            ]
        }
    ),

    html.H2("*** Line Graph *** "),
    dcc.Graph(
        id="exm2",
        figure={
            "data": [
                {"x": [1, 3, 5], "y": [10, 12, 14], "type": "line", "name": "exmple3"},
                {"x": [2, 4, 6], "y": [13, 15, 17], "type": "line", "name": "exmple4"}
            ]
        }
    ),

    html.H2("*** Scatter Plot Graph *** "),
    dcc.Graph(
        id="exm3",
        figure={
            "data": [
                {"x": [1, 3, 5, 7], "y": [10, 12, 14, 16], "type": "scatter", "mode": "markers", "name": "scatter exmpl1"},
                {"x": [2, 4, 6, 8], "y": [13, 15, 17, 19], "type": "scatter", "mode": "markers", "name": "scatter exmpl2"}
            ]
        }
    ),

    html.H2("*** Pie Chart Graph *** "),
    dcc.Graph(
        id="exm4",
        figure={
            "data": [
                {"labels": ["A", "B", "C"], "values": [10, 12, 14], "type": "pie", "name": "pie chart expl1"},
            ],
            "layout": {"title": "pie chart example"}
        }
    ),
])

# Lien avec FastAPI
server = app.server
