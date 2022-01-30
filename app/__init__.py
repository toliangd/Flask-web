from flask import Flask, sessions
from web.config import Config

# создали экземпляр класса Flask
app = Flask(__name__)
app.config.from_object(Config)

# импортируем вьюхи
from web.app import view
