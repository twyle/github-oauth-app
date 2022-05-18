# -*- coding: utf-8 -*-
"""This module tests the helper methods in the API/helpers.py module."""


from os import access

import pytest

from API.helpers import get_access_token, get_user_data


def test_get_access_token():
    """Tests that get_access_token returns a valid string.

    GIVEN a client id, client secret and a request token
    WHEN we call get_access_token
    THEN we should get back the access token which is a string

    """
    # Still under development; mock the request made to GitHub

    assert True


def test_get_access_token_empty_client_id(get_auth_parameters):
    """Tests that get_access_token raise the ValueError on empty client id.

    GIVEN an empty client id, client secret and a request token
    WHEN we call get_access_token
    THEN the function should raise a ValueError

    """
    CLIENT_ID = ''
    CLIENT_SECRET = get_auth_parameters[1]
    request_token = get_auth_parameters[2]

    with pytest.raises(ValueError):
        get_access_token(CLIENT_ID, CLIENT_SECRET, request_token)


def test_get_access_token_empty_client_secret(get_auth_parameters):
    """Tests that get_access_token raise the ValueError on empty client secret.

    GIVEN an empty client secret, client id and a request token
    WHEN we call get_access_token
    THEN the function should raise a ValueError

    """
    CLIENT_ID = get_auth_parameters[0]
    CLIENT_SECRET = ''
    request_token = get_auth_parameters[2]

    with pytest.raises(ValueError):
        get_access_token(CLIENT_ID, CLIENT_SECRET, request_token)


def test_get_access_token_empty_request_token(get_auth_parameters):
    """Tests that get_access_token raise the ValueError on empty request token.

    GIVEN a client secret, client id and an empty request token
    WHEN we call get_access_token
    THEN the function should raise a ValueError

    """
    CLIENT_ID = get_auth_parameters[0]
    CLIENT_SECRET = get_auth_parameters[1]
    request_token = ''

    with pytest.raises(ValueError):
        get_access_token(CLIENT_ID, CLIENT_SECRET, request_token)


def test_get_access_token_non_string_client_id(get_auth_parameters):
    """Tests that get_access_token raise the ValueError on non-string client id.

    GIVEN a non-string client id, client secret and a request token
    WHEN we call get_access_token
    THEN the function should raise a ValueError

    """
    CLIENT_ID = 4
    CLIENT_SECRET = get_auth_parameters[1]
    request_token = get_auth_parameters[2]

    with pytest.raises(ValueError):
        get_access_token(CLIENT_ID, CLIENT_SECRET, request_token)


def test_get_access_token_numeric_client_secret(get_auth_parameters):
    """Tests that get_access_token raise the ValueError on numeric client secret.

    GIVEN a numeric client secret, client id and a request token
    WHEN we call get_access_token
    THEN the function should raise a ValueError

    """
    CLIENT_ID = get_auth_parameters[0]
    CLIENT_SECRET = 4
    request_token = get_auth_parameters[2]

    with pytest.raises(ValueError):
        get_access_token(CLIENT_ID, CLIENT_SECRET, request_token)


def test_get_access_token_numeric_request_token(get_auth_parameters):
    """Tests that get_access_token raise the ValueError on numeric request token.

    GIVEN a client secret, client id and an numeric request token
    WHEN we call get_access_token
    THEN the function should raise a ValueError

    """
    CLIENT_ID = get_auth_parameters[0]
    CLIENT_SECRET = get_auth_parameters[1]
    request_token = 4

    with pytest.raises(ValueError):
        get_access_token(CLIENT_ID, CLIENT_SECRET, request_token)


def test_get_user_data():
    """Tests that get_user_data returns a valid dictionary.

    GIVEN an access token
    WHEN we call get_user_data
    THEN we should get back the user data which is a dictopnary

    """
    # Still under development; mock the request made to GitHub

    assert True


def test_get_user_data_empty_access_token():
    """Tests that get_user_data raises a ValueError on empty access token.

    GIVEN an empty access token
    WHEN we call get_user_data
    THEN the mathod should raise a ValueError

    """
    access_token = ''
    with pytest.raises(ValueError):
        get_user_data(access_token)


def test_get_user_data_numeric_access_token():
    """Tests that get_user_data raises a ValueError on numeric access token.

    GIVEN a numeric access token
    WHEN we call get_user_data
    THEN the mathod should raise a ValueError

    """
    access_token = 4
    with pytest.raises(ValueError):
        get_user_data(access_token)
