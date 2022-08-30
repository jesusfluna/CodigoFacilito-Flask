from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hola mundo!!"


#
@app.route('/params/<name>/<int:num>')#especificamos el tipo del ultimo parametro a entero "params/juan/5"
@app.route('/params/<name>/')#"params/juan"
@app.route('/params/')#"params/"
def parametros(name='este es un valor por default', num=0):
    return "Los params valen: {}, {}".format(name, num)


if __name__=='__main__':
    app.run(debug=True, port=8000)