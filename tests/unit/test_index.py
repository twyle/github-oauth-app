# -*- coding: utf-8 -*-
"""This module tests the index route."""


def test_index(client):
    """Tests that the index route returns ok message on GET request.

    GIVEN we have the /index route
    WHEN we send a GET request
    THEN we should get a 200 OK response
    """
    resp = client.get('/index')
    assert resp.status_code == 200


def test_index_bad_http_method(client):
    """Tests that the index route returns method not allowed message on POST request.

    GIVEN we have the /index route
    WHEN we send a POST request
    THEN we should get a 405 error code in the response
    """
    resp = client.post('/index')
    assert resp.status_code == 405
