# -*- coding: utf-8 -*-
"""This module creates the routes for our API."""

from flask import render_template, request

from API import app


@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index() -> dict:
    """Handle get requests to /index route.

    Returns
    -------
    data: dict
        A dictionary showing:
        {
            "data": "Hello from github oauth json endpoint!"
        }
    """
    data = {
        "data": 'Hello from github oauth json endpoint!'
    }

    return data, 200


@app.route('/home', methods=['GET'])
def home() -> str:
    """Provide the user with the option to register with GitHub."""
    return render_template('index.html', client_id=app.config['CLIENT_ID']), 200


@app.route('/github/callback', methods=['GET'])
def github_callback():
    """Authenticate the user."""
    # get_request_token()
    # get_access_token()
    # get_user_data()
    args = request.args
    request_token = args.get('code')
    return request_token
