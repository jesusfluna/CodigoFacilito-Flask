from flask import Flask
from flask import render_template
import forms #importamos nuestro fichero py con los formularios

app = Flask(__name__)


@app.route("/")
def index():
    comment_form = forms.CommentForm()#Creamos un objeto de la clase formulario
    title = "Curso flask"
    return render_template('index.html', title=title, form = comment_form)#Enviamos el formulario como un objeto mas a la vista


if __name__ == '__main__':
    app.run(debug=True,port=8000)