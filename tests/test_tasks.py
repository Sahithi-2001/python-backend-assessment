import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test task",
            "description": "Testing backend",
            "github_repo": "tiangolo/fastapi"
        }
    )
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_task_not_found():
    response = client.get("/tasks/non-existent-id")
    assert response.status_code == 404
