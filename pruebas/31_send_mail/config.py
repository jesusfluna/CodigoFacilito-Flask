import os


class Config(object):
    SECRET_KEY = 'supercalifragilisticoespialidoso'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = "" #aqui va el mail
    MAIL_PASSWORD = "" #aqui va la pass del mail


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ="postgresql://postgres:inerco@localhost/demo" #Cadena de conexion con la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    