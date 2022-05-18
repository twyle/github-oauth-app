# -*- coding: utf-8 -*-
"""This module contains initialization code for the API package."""

from flask import Flask

from API.config import DevelopmentConfig
from API.helpers import set_flask_environment

app = Flask(__name__)

set_flask_environment(app=app)

from API import routes
