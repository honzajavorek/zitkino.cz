# -*- coding: utf-8 -*-


__version__ = '2.1.dev'


import logging

from flask import Flask
from flask.ext.assets import Environment as Assets

from .mongo import MongoEngine


app = Flask(__name__)
app.config.from_object('zitkino.config')
logging.basicConfig(**app.config['LOGGING'])


assets = Assets(app)
db = MongoEngine(app)


from zitkino import views, templating  # NOQA