from wtforms import Form, StringField, EmailField, TextAreaField
from wtforms import validators  # Importamos los validadores
import email_validator


class CommentForm(Form):
    # Añadimos mediante un array de validators las restricciones de cada campo
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
