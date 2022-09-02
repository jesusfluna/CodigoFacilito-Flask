from flask import Flask, render_template, request, make_response
from flask_wtf import CSRFProtect
import forms

app = Flask(__name__)
app.secret_key = 'supercalifragilisticoespialidoso'
csrf = CSRFProtect(app)


@app.route("/")
def index():
    custome_cookie = request.cookies.get('CookiePrueba', 'Undefined')#Leemos el valor de la cookie a partir de su nombre, el segundo valor es el valor resultado en caso de no encontrar la cookie
    print(custome_cookie)
    title = "Curso flask"
    return render_template('index.html', title=title)


#gestion de cookies
@app.route("/cookie", methods=['GET', 'POST'])
def cookie():
    response = make_response(render_template('cookie.html')) #Necesitamos un response para gestionar las cookies
    response.set_cookie('CookiePrueba', 'pruebaFlask') #Creamos la cookie con el primer parametro como nombre y el segundo como data
    return response


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = forms.LoginForm()
    return render_template('login.html', form=login_form)


@app.route("/comment", methods=['GET', 'POST'])
def comment():
    comment_form = forms.CommentForm(request.form)

    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print("Error en el formulario")

    title = "Curso flask"
    return render_template('comment.html', title=title, form=comment_form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
