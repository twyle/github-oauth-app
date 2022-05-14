# -*- coding: utf-8 -*-
"""This module creates the routes for our API."""

from API import app


@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index() -> dict:
    """Handle get requests to /index route.

    Returns
    -------
    dict:
        A dictionary showing:
        {
            "data": 'Hello from github oauth json endpoint'
        }
    """
    data = {
        "data": 'Hello from github oauth json endpoint'
    }

    return data, 200
