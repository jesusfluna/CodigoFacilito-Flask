from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hola mundo!!"


@app.route('/saluda')
def saluda():
    return "Hola, que tal está?"


@app.route('/params')
def parametroGet():
    param1 = request.args.get('param1','null1')#recogemos un parametro en formato '?params1=1', y le establecemos un valor default de 'null1'
    param2 = request.args.get('param2','null2')  # recogemos un parametro en formato '?params1=1&param2=2', y le establecemos un valor default de 'null2'
    return "El parametro 1 vale: "+param1+" y el parametro 2 vale:"+param2

if __name__=='__main__':
    app.run(debug=True, port=8000)