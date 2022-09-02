from wtforms import Form, StringField, EmailField, TextAreaField, validators
from wtforms import HiddenField


def length_honeypot(form, field):#funcion que usaremos como validator propio para el campo honeypot
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
    ])#Validacion propia para simular un honeypot o campo 'trampa' para atacantes
