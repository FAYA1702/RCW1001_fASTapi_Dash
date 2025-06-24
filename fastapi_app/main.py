import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.templating import Jinja2Templates
import uvicorn
from dash_app import app as app_dash
from datetime import datetime
import requests


# creeer l'objet de FastApi
app = FastAPI()

# Obtenir le chemin absolu vers le repertoire des modeles
templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"templates"))

# Obtenir le chemin absolu vers le repertoire statique
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"static"))

# configurer le modele Jinja2 pour le rendu des fichires HTML
templates = Jinja2Templates(directory=templates_dir)

# servir des fichiers statiques
# app.mount("/static", StaticFiles(directory=static_dir))
app.mount("/static", StaticFiles(directory=static_dir), name="static")

#Montez l'application Dash sou le chemain /dashboard
app.mount("/dashboard", WSGIMiddleware(app_dash.server))

user={"admin":"123"}

@app.get("/")
async def home_page(request:Request):
    now = datetime.now()
    info = {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "weather": {
            "city": "Montréal",
            "temperature": "21°C",
            "description": "Ensoleillé"
        }
    }
    return templates.TemplateResponse('home.html', {"request":request,"info":info})


@app.get("/login")
async def login_page(request:Request):
    return templates.TemplateResponse('login.html', {"request":request})


@app.post("/login")
async def login(request: Request, username:str = Form(...), password: str = Form(...)):
    if username in user and user[username] == password:
        response = RedirectResponse(url='/dashboard', status_code=302)
        response.set_cookie(key="Authorization", value="Bearer Token", httponly=True)
        return response
    return templates.TemplateResponse("login.html",{"request":request, "error":"Invalid username and password"})


@app.get("/logout")
async def logout():
    response = RedirectResponse(url='/login')
    response.delete_cookie('Authorization')
    return response


@app.get("/info")
async def get_info():
    now = datetime.now()
    return {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "weather": {
            "city": "Montréal",
            "temperature": "21°C",
            "description": "Ensoleillé"
        }
    }
import requests

def fetch_weather_info():
    try:
        response = requests.get("http://rcw1002-projet-2-hjgzchcbayepbbfe.canadacentral-01.azurewebsites.net/info", timeout=2)
        return response.json()
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
