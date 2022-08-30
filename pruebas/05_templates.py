from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='../templates')#si no usamos el directorio de templates por defecto, aqui se especifica la nueva ruta


@app.route('/')
def index():
    return render_template('index1.html')#carga el template index.html que por defecto es buscado en un directorio templates del mismo nivel


if __name__=='__main__':
    app.run(debug=True, port=8000)