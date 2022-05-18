# -*- coding: utf-8 -*-
"""This module tests the home route."""


def test_home(client):
    """Tests that the home route returns ok message on GET request.

    GIVEN we have the /home route
    WHEN we send a GET request
    THEN we should get a 200 OK response
    """
    resp = client.get('/home')
    assert resp.status_code == 200


def test_home_bad_http_method(client):
    """Tests that the home route returns method not allowed message on POST request.

    GIVEN we have the /home route
    WHEN we send a POST request
    THEN we should get a 405 error code in the response
    """
    resp = client.post('/home')
    assert resp.status_code == 405
