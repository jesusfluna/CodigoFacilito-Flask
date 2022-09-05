from flask import Flask, render_template, request, make_response, url_for
from flask_wtf import CSRFProtect
import forms
from flask import session #Importamos la libreria de gestion de sesiones de flask
from flask import redirect #Libreria flask para redireccion web

app = Flask(__name__)
app.secret_key = 'supercalifragilisticoespialidoso' #Necesario para trabajar con sesiones
csrf = CSRFProtect(app)


@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        print(username)
    custome_cookie = request.cookies.get('CookiePrueba', 'Undefined')
    print(custome_cookie)
    title = "Index"
    return render_template('index.html', title=title)


@app.route("/cookie", methods=['GET', 'POST'])
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('CookiePrueba', 'Cookie pruebaFlask')
    return response


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == "POST" and login_form.validate():
        session['username'] = login_form.username.data #Se crea una variable de sesion llamada username con el valor del campo username del formulario
    return render_template('login.html', form=login_form)


@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')

    return redirect(url_for('login'))


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
