from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = "John Doe"
    return render_template('index.html', name=name)


@app.route('/client')
def client():
    list_name = ["John Doe","juan perez","Mario Rosi"]
    return render_template('client.html', list_name=list_name)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

    """
    # RingaTechIA
    Ejemplos de prueba de IA con Python siguiendo RingaTech
    
    
    # 01-CelsiusToFahrenheit
    Red neuronal simple para transformacion de un valor en Celsius a otro en Fahrenheits
    
    # 02-ClasificadorRopa
    Clasificador de imagenes 28x28 en blanco y negro con un dataset de tendorflow.
    """