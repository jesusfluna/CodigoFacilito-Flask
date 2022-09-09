from flask import Flask, render_template, request, make_response, url_for, session, redirect, flash, g
from flask_wtf import CSRFProtect
import forms
import json
from config import DevelopmentConfig
from models import db, User

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/ajax-login', methods=['POST'])
def ajaxlogin():
    print(request.form)
    username = request.form['username']
    response = {'status': 200, 'username': username, 'id': 1}
    return json.dumps(response)


@app.before_request
def before_request():
    g.test = "Before"
    print(g.test)


@app.after_request
def after_request(response):
    g.test = "After"
    print(g.test)
    return response


@app.route("/")
def index():
    print(g.test)
    if 'username' in session:
        username = session['username']
        print(username)
    custome_cookie = request.cookies.get('CookiePrueba', 'Undefined')
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
        flash("Bienvenido {}".format(username))
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


# logica de la creacion de un usuario usando el modelo User
@app.route("/create", methods=['GET', 'POST'])
def create():
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
        user = User(create_form.username.data,
                    create_form.email.data,
                    create_form.password.data)

        db.session.add(user)
        db.session.commit()

        success_message = "Usuario registrado en la base de datos"
        flash(success_message)

    return render_template("create.html", form=create_form)


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5555)


