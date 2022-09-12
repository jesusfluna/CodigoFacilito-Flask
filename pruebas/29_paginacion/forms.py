from wtforms import Form, StringField, EmailField, TextAreaField, validators, PasswordField
from wtforms import HiddenField
from models import User


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')


class CommentForm(Form):
    # username = StringField('username', validators=[
    #     validators.data_required(message="Valor requerido"),
    #     validators.length(min=4, max=25, message="Valor requerido")
    # ])
    # email = EmailField('Email', validators=[
    #     validators.data_required(message="Valor requerido"),
    #     validators.Email(),
    #     validators.length(max=100, message="No puede tener mas de 100 caracteres")
    # ])
    comment = TextAreaField('Comentario',
                            validators=[validators.length(max=240, message="No puede tener mas de 240 caracteres")])

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


class CreateForm(Form):
    username = StringField('Username', validators=
                           [
                               validators.data_required(message='El username es requerido'),
                               validators.length(min=4, max=50, message='Ingrese un username valido')
                           ])
    email = EmailField('Correo electronico', validators=
                       [validators.data_required(message='El email es requerido!.'),
                        validators.Email(message='Ingrese un email valido'),
                        validators.length(min=4, max=50, message='Ingrese un email valido')
                        ])
    password = PasswordField('Password', validators=[validators.data_required(message='El password es requerido')])

    """ cada campo del formulario internamente tendra una funcion validate_ asociada, lo que vamos a hacer es sobrescribir la de username"""
    def validate_username(self,field):
        username = field.data
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError("Ya hay un usuario con ese username")




