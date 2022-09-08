from wtforms import Form, StringField, EmailField, TextAreaField, validators, PasswordField
from wtforms import HiddenField


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')


class CommentForm(Form):
    username = StringField('username', validators=[
        validators.data_required(message="Valor requerido"),
        validators.length(min=4, max=25, message="Valor requerido")
    ])
    email = EmailField('Email', validators=[
        validators.data_required(message="Valor requerido"),
        validators.Email(),
        validators.length(max=100, message="No puede tener mas de 100 caracteres")
    ])
    comment = TextAreaField('Comentario', validators=[validators.length(max=240, message="No puede tener mas de 240 caracteres")])

    honeypot = HiddenField('', validators=[
        length_honeypot
    ])


class LoginForm(Form):
    username = StringField('Username', validators=[
        validators.data_required(message='El username es un dato requerido'),
        validators.length(min=4, max=20, message='El tamaño tiene que estar entre 4 y 20 caracteres')
    ])
    password = PasswordField('Password', validators=[
        validators.data_required(message='La contraseña es un dato requerido')
    ])