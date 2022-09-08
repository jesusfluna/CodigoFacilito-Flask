import os


class Config(object):
    SECRET_KEY = 'supercalifragilisticoespialidoso'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ="postgresql://postgres:inerco@localhost/demo" #Cadena de conexion con la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
