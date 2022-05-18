# -*- coding: utf-8 -*-
"""This module contain the confuguration for the application."""
import os

from dotenv import load_dotenv

load_dotenv()


class BaseConfig():
    """Base configuration."""

    SECRET_KEY = 'SECRET_KEY'
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class TestingConfig(BaseConfig):
    """Configuration used during testing."""

    SECRET_KEY = 'SECRET_KEY'
    DEBUG = True
    TESTING = True


class DevelopmentConfig(BaseConfig):
    """Configuration used during development."""

    SECRET_KEY = 'SECRET_KEY'
    DEBUG = True
    TESTING = False

    CLIENT_ID = os.environ['CLIENT_ID']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']


class StagingConfig(BaseConfig):
    """Configuration used during staging."""

    SECRET_KEY = 'SECRET_KEY'
    DEBUG = True
    TESTING = False

    CLIENT_ID = os.environ['CLIENT_ID']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']


class ProductionConfig(BaseConfig):
    """Configuration used during production."""

    SECRET_KEY = 'SECRET_KEY'
    DEBUG = False
    TESTING = False

    CLIENT_ID = os.environ['CLIENT_ID']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']
