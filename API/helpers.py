# -*- coding: utf-8 -*-
"""This module has methods that are used in the other modules in this package."""

import os

import requests


def set_flask_environment(app) -> str:
    """Set the flask development environment.

    Parameters
    ----------
    app: flask.Flask
        The flask application object

    Raises
    ------
    KeyError
        If the FLASK_ENV environment variable is not set.

    Returns
    -------
    str:
        Flask operating environment i.e development

    """
    if os.environ['FLASK_ENV'] == 'production':  # pragma: no cover
        app.config.from_object('API.config.ProductionConfig')
    elif os.environ['FLASK_ENV'] == 'development':  # pragma: no cover
        app.config.from_object('API.config.DevelopmentConfig')
    elif os.environ['FLASK_ENV'] == 'test':
        app.config.from_object('API.config.TestingConfig')

    return os.environ['FLASK_ENV']


def get_access_token(CLIENT_ID: str, CLIENT_SECRET: str) -> str:
    """Obtain the access token from github.

    Given the clint id and client secret issued out by GitHub, this method
    should give backan access token

    Parameters
    ----------
    CLIENT_ID: str
        A string representing the client id issued out by github
    CLIENT_SECRET: str
        A string representing the client secret issued out by github

    Throws
    ------
    ValueError:
        if CLIENT_ID or CLIENT_SECRET is empty or not a string

    Returns
    -------
    access_token: str
        A string representing the access token issued out by github
    """
    if not CLIENT_ID:
        raise ValueError('The CLIENT_ID has to be supplied!')
    if not CLIENT_SECRET:
        raise ValueError('The CLIENT_SECRET has to be supplied!')
    if not isinstance(CLIENT_ID, str):
        raise ValueError('The CLIENT_ID has to be a string!')
    if not isinstance(CLIENT_SECRET, str):
        raise ValueError('The CLIENT_SECRET has to be a string!')

    url = f'https://github.com/login/oauth/authorize?client_id={ CLIENT_ID }'

    return url
