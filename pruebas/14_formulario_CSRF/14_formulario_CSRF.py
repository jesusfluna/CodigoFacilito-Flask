from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
import forms

app = Flask(__name__)
app.secret_key = 'supercalifragilisticoespialidoso' #Secretkey para proteger el acceso a nuestra aplicacion
csrf = CSRFProtect(app) #Encriptamos la key


@app.route("/")
def index():
    title = "Curso flask"
    return render_template('index.html', title=title)


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
