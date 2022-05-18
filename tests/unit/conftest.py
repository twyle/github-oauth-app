# -*- coding: utf-8 -*-
"""This module sets up the fixtures that will be used in our testing."""

import pytest

from API import app


@pytest.fixture
def client():
    """Create the test client."""
    test_client = app.test_client()
    return test_client


@pytest.fixture
def get_auth_parameters():
    """Generate the auth parameters."""
    CLIENT_ID = app.config['CLIENT_ID']
    CLIENT_SECRET = app.config['CLIENT_SECRET']
    request_token = 'request token'

    return CLIENT_ID, CLIENT_SECRET, request_token


@pytest.fixture
def get_access_token_parameters():
    """Generate a dummy access token."""
    return "acess token"
