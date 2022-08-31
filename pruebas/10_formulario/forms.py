from wtforms import Form,StringField,EmailField,TextAreaField;


class CommentForm(Form):#Definicion de formularios, cada formulario es una clase donde cada campo del formulario es uno de los atributos de la clase
    username = StringField('username')
    email = EmailField('Email')
    comment = TextAreaField('Comentario')