# -*- coding: utf-8 -*-
"""This module contains initialization code for the API package."""

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)


from API import routes
