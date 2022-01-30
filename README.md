import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = 'SECRET-KEY'
    BD_PASS = 'BD-PASS'
    DB_LOGIN = 'DB-PASS'
    DB_ADDRESS = '127.0.0.1'
    DB_NAME = 'webauth'
    SALT = '1w2e3r4r5t6y'