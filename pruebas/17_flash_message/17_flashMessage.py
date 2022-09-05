from flask import Flask, render_template, request, make_response, url_for, session, redirect
from flask_wtf import CSRFProtect
import forms
from flask import flash

app = Flask(__name__)
app.secret_key = 'supercalifragilisticoespialidoso'
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
        username = login_form.username.data
        flash("Bienvenido {}".format(username))#mediante flash enviamos al cliente el mensaje creado
        session['username'] = login_form.username.data
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
