import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "Test User"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

def test_get_user():
    response = client.post("/users/", json={"name": "Test User"})
    user_id = response.json()["id"]

    response = client.get(f"/users/{user_id}/")
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

def test_update_user():
    response = client.post("/users/", json={"name": "Test User"})
    user_id = response.json()["id"]

    response = client.put(f"/users/{user_id}/", json={"name": "Updated User"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"

def test_search_users():
    response = client.get("/users/search/?query=test")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
