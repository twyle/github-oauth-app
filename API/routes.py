# -*- coding: utf-8 -*-
"""This module creates the routes for our API."""

from flask import render_template, request

from API import app
from API.helpers import get_access_token, get_user_data


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
    return render_template('home.html', client_id=app.config['CLIENT_ID']), 200


@app.route('/github/callback', methods=['GET'])
def github_callback():
    """Authenticate the user and displays their data."""
    args = request.args
    request_token = args.get('code')
    print(f'The request token {request_token}')

    CLIENT_ID = app.config['CLIENT_ID']
    CLIENT_SECRET = app.config['CLIENT_SECRET']
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, request_token)

    user_data = get_user_data(access_token)
    return render_template('dashboard.html', userData=user_data)
