from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')
app.run('127.0.0.1', port=5000)

@app.route("/")
def hello_world():
    #return "<p>Bienvenido, Grupo Zhumir-A!</p>"
    return render_template("index.html")

@app.route("/lascasas")
def las_casas():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/casas/",
            auth=('admin', 'admin'))
    casas = json.loads(r.content)['results']
    numero_casas = json.loads(r.content)['count']
    return render_template("casas.html", casas=casas,
    numero_casas=numero_casas)

@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/departamentos/",
            auth=('admin', 'admin'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("departamentos.html", datos=datos,
    numero=numero)

@app.route("/losbarrios")
def los_barrios():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/barrios/",
            auth=('admin', 'admin'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("barrios.html", datos=datos,
    numero=numero)

@app.route("/laspersonas")
def las_personas():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/personas/",
            auth=('admin', 'admin'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("personas.html", datos=datos,
    numero=numero)


# funciones ayuda

def obtener_casa(url):
    """
    """
    r = requests.get(url, auth=('admin', 'admin'))
    nombre_casa = json.loads(r.content)['nombre']
    return nombre_casa

def obtener_departamento(url):
    """
    """
    r = requests.get(url, auth=('admin', 'admin'))
    nombre_departamento = json.loads(r.content)['nombre']
    return nombre_departamento
