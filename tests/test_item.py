import pytest


def test_home_page(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    AND the response contains `Hello, world!`
    """

    response = client.get('/')
    assert response.status_code == 200
    assert "Hello, world!" in response.text
