from flask import Flask, render_template, request #importamos el request para gestionar los datos entrantes por el formulario
import forms

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])#Por defecto la ruta solo admite el metodo GET, añadiendo ' methods=['GET', 'POST']' permite tambien el post
def index():
    comment_form = forms.CommentForm(request.form)#Con el request.form trae los datos de una request realizada en el formulario, si no la hubiese como al inicio, crea el formulario en blanco

    if request.method == 'POST':#Comprobamos que se ha utilizado el metodo post y vemos el contenido de los campos
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)

    title = "Curso flask"
    return render_template('index.html', title=title, form=comment_form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
