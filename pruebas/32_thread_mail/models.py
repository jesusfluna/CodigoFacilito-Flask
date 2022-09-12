from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(120))
    comments = db.relationship("Comment")#atributo ara enlazar con en modelo relacionado. CUIDADo se indica el nombre de la class del modelo
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.__create_password(password)

    def __create_password(self, password):
            return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


 #Nuevo modelo para probar las relaciones n:m
class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Campo foraneo para crear la relacion entre tablas, Cuidado, se indica el nombre de la tabla, que en este caso coincide con la clase
    text = db.Column(db.Text())
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
