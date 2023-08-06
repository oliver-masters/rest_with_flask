import pytest
from src import create_app, db


# Fixture to create and configure a test Flask app
@pytest.fixture(scope="module")
def test_app():
    app = create_app("sqlite:///test_data.db")
    app_context = app.app_context()
    app_context.push()
    yield app
    app_context.pop()


# Fixture to create a test client for the Flask app
@pytest.fixture(scope="module")
def client(test_app):
    return test_app.test_client()


# Fixture to create and set up a test database
@pytest.fixture(scope="function")
def db_testing(test_app):
    db.create_all()

    yield db

    db.session.remove()
    db.drop_all()
