from fastapi.testclient import TestClient

from src.api.api import app

client = TestClient(app)


def test_hello_world():
    query = {"query": "teste"}
    response = client.post("/", json=query)

    assert response.status_code == 200
    assert response.json() == {"mensagem_recebida": "teste"}
