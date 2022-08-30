from flask import Flask

app = Flask(__name__)


@app.route('/')#indica una ruta de entrada para una peticion
def index():#Metodo que se iniciara al lanzarse la peticion anterior
    return "Hola mundo!!"

app.run()#Ejecuta el servidor por defecto en el puerto 50000