import json
from src.models import StoreModel


def test_create_store(client, db_testing):
    """
    Feature: Add new store

    Scenario: Add a store
        GIVEN a Flask application configured for testing
        WHEN a store is created
        THEN a 201 response is returned
        AND a new store is added to the database
    """
    stores = StoreModel.query.all()
    assert len(stores) == 0

    store_name = "My First Store"
    data = {"name": store_name}
    response = client.post('/store', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert store_name in response.text

    stores = StoreModel.query.all()
    assert len(stores) == 1
    assert stores[0].name == store_name
