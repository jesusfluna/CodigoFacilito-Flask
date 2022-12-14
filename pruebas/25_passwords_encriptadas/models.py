from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash #importacion para generar un hash de la contraseña del usuario
import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(120))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.__create_password(password)

    def __create_password(self, password):
            return generate_password_hash(password)
