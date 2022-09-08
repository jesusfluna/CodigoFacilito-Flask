import os


class Config(object):
    SECRET_KEY = 'supercalifragilisticoespialidoso'


class DevelopmentConfig(Config):
    DEBUG = True